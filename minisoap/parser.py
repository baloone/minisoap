# Copyright (C) 2019 Mohamed H
# 
# This file is part of Minisoap.
# 
# Minisoap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Minisoap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Minisoap.  If not, see <http://www.gnu.org/licenses/>.

"""
Sequence = Expression|Name=Expression
N = [a-Z'_$][a-Z'_$0-9]*
Expression' = Expression' Expression | Expression
E = Name Expression' | '.*' | [0-9]+ | (Expression)
"""

class LineParsingError(Exception):
    pass

class ContinueParsing(Exception):
    def __init__(self, vn=None, pile = None, txt = None):
        Exception.__init__(self)
        self.vn = vn
        self.pile = pile
        self.txt = txt

class Sequence:
    def __init__(self, a1, a2=None):
        self.type = 'assign' if a2!=None else 'call'
        self.variable_name = a1 if a2!= None else None
        self.expr = a2 if a2!=None else a1
    def __str__(self):
        return 'Sequence('+self.variable_name.__str__()+', '+self.expr.__str__()+')'

class Help(Sequence):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Help('+self.name+')'

class Expr:
    def __init__(self, val, *args):
        self.val = val
        self.args = args
    def __str__(self):
        s = ', '.join(map(lambda x: x.__str__(), self.args))
        return 'Expr('+self.val.__str__()+', '+s+')'
        
class String(Expr):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'String('+self.val+')'
        
class Transition(Expr):
    def __init__(self, table):
        self.table = table
    def __str__(self):
        return 'Transition('+".\t".join([str(t[0])+" ->> "+str(t[1]) for t in self.table])+')'

class Number(Expr):
    def __init__(self, val):
        self.val = float(val)
    def __str__(self):
        return 'Number('+str(self.val)+')'

class VariableName(Expr):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'VariableName('+self.val+')'


class Parser:
    def __init__(self):
        self._w = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['\'', '_', "$"]
        self._n = [chr(i) for i in range(48, 58)]
        self._wn = self._w + self._n
        self._wh = [' ', '\t']
        self._pile = []
        self._brkts = ''
        self._f = ''
    def parse_line(self, line, continueparsing=None):
        if continueparsing!=None:
            vn = continueparsing.vn 
            if vn==None:
                e = self.parse_expr(line, continueparsing)
                return Sequence(e) if e != None else None 
            else:
                return Sequence(vn,self.parse_expr(line, continueparsing))
        l = line[:(line.index('//'))] if '//' in line else line
        cur = 0
        while cur < len(l) and l[cur] in self._wh:
            cur+=1
        if cur >= len(l):
            return None
        if l[cur] in self._w:
            name = ''
            while cur < len(l)-1 and l[cur] in self._wn:
                name += l[cur]
                cur+=1
            while cur < len(l)-1 and l[cur] in self._wh:
                cur+=1
            if l[cur] == "=":
                try:
                    return Sequence(VariableName(name), self.parse_expr(l[cur+1:]))
                except ContinueParsing as cp:
                    raise ContinueParsing(vn=VariableName(name), pile=cp.pile, txt=cp.txt)
            elif l[cur] == "?":
                for i in l[cur+1:]:
                    if not i in self._wh:
                        break
                else:
                    return Help(name)
        e = self.parse_expr(l)
        return Sequence(e) if e != None else None
    def parse_expr(self, t, continueparsing=None):
        cur = 0
        funcs = [getattr(self, f) for f in dir(Parser) if f.startswith("_Parser")]
        pile = []
        try:
            if continueparsing != None:
                ep, cur = self.__get_brackets(t, cur, continueparsing)
                pile.append(ep)
            while cur < len(t):
                cur = self.__skip_white_space(t, cur)
                for f in funcs:
                    e = f (t, cur)
                    if e != None:
                        ep, cur = e
                        pile.append(ep)
                        break
                else:
                    raise LineParsingError('Unexpected character: '+t[cur], cur)
        except ContinueParsing as cp:
            raise ContinueParsing(pile=pile,txt=cp.txt)
        if len(pile) > 1 and not isinstance(pile[0], VariableName):
            raise LineParsingError('Calling a non callable')
        if len(pile) < 1:
            return None
        if len(pile) == 1:
            return pile[0]
        return Expr(pile[0], *pile[1:])
    def parse_transition(self, txt):
        table = []
        for l in txt.split(";"):
            if l.replace(' ', '').replace('\t', '') == "": continue
            [time, amplitude] = [i.replace(' ', '').replace('\t', '') for i in l.split(':')]
            if time[-2:] == "ms": table.append((int(time[:-2]), float(amplitude)))
            else: table.append((int(float(time[:-1])*1000), float(amplitude)))
        return Transition(table)
    def __skip_white_space(self, t, i):
        cur = i
        while t[cur] in self._wh and cur < len(t)-1:
            cur+=1
        return cur
    def __get_string(self, t, i):
        cur = i
        if t[cur] != '"' : return None
        s = ''
        while t[cur+1] != '"':
            cur+=1
            s+=t[cur]
        cur+=2
        if cur < len(t) and not t[cur] in self._wh : raise LineParsingError('Expected whitespace after string', cur)
        return String(s),cur
    def __get_variable_name(self, t, i):
        cur = i
        if not t[cur] in self._w : return None
        vn = t[cur]
        while cur < len(t)-1 and t[cur+1] in self._wn :
            cur+=1
            vn+=t[cur]
        cur+=1
        if cur < len(t) and not t[cur] in self._wh : raise LineParsingError('Expected whitespace after variable name', cur)
        return VariableName(vn),cur
    def __get_parenthesis(self, t, i):
        cur = i
        if t[cur] != '(': return None
        _t = ''
        d = cur+1
        p = 0
        try:
            while t[cur+1] != ')' or p:
                if t[cur+1] == '(': p+=1
                if t[cur+1] == ')': p-=1
                if p < 0: raise LineParsingError('Unexpected parenthesis', cur)
                cur+=1
                _t+=t[cur]
        except IndexError:
            raise LineParsingError('Parenthesis not closed', cur)
        cur+=2
        return self.parse_expr(t[d:cur-1]),cur
    def __get_brackets(self, t, i, continueparsing=None):
        brkts='' if continueparsing==None else continueparsing.txt+' '
        cur = i
        if continueparsing == None:
            if t[cur] != '{': return None
            else:cur+=1
        try:
            while t[cur] != '}':
                brkts+=t[cur]
                cur+=1
        except IndexError:
            raise ContinueParsing(txt=brkts)
        cur+=1
        return self.parse_transition(brkts),cur
    def __get_number(self, t, i):
        cur = i
        comma = False
        if not t[cur] in self._n and not t[cur] == '.': return None
        a = t[cur]
        while cur < len(t)-1 and (t[cur+1] in self._n or t[cur+1] == '.'):
            if t[cur+1] == '.':
                if comma: 
                    raise LineParsingError("Not a number", cur)
                else:
                    comma = True
            cur+=1
            a+=t[cur]
        cur+=1
        if cur < len(t) and not t[cur] in self._wh : raise LineParsingError('Expected whitespace after number', cur)
        return Number(float(a)), cur

