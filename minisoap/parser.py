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

w = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)] + ['\'', '_', "$"]
n = [chr(i) for i in range(48, 58)]
wn = w + n
wh = [' ', '\t']

def parse_line(line):
    l = line[:(line.index('//'))] if '//' in line else line
    cur = 0
    while l[cur] in wh:
        cur+=1
        if cur >= len(l):
            return None
    if l[cur] in w:
        name = ''
        while l[cur] in wn and cur < len(l)-1:
            name += l[cur]
            cur+=1
        while l[cur] in wh and cur < len(l)-1:
            cur+=1
        if l[cur] == "=":
            return Sequence(VariableName(name), parse_expr(l[cur+1:]))
        elif l[cur] == "?":
            for i in l[cur+1:]:
                if not i in wh:
                    break
            else:
                return Help(name)
        
    e = parse_expr(l)
    return Sequence(e) if e != None else None



def parse_expr(t):
    cur = 0
    def skip_white_space(t, i):
        cur = i
        while t[cur] in wh and cur < len(t)-1:
            cur+=1
        return cur
    def get_string(t, i):
        cur = i
        if t[cur] != '"' : return None
        s = ''
        while t[cur+1] != '"':
            cur+=1
            s+=t[cur]
        cur+=2
        if cur < len(t) and not t[cur] in wh : raise LineParsingError('Expected whitespace after string', cur)
        return String(s),cur
    def get_variable_name(t, i):
        cur = i
        if not t[cur] in w : return None
        vn = t[cur]
        while cur < len(t)-1 and t[cur+1] in wn :
            cur+=1
            vn+=t[cur]
        cur+=1
        if cur < len(t) and not t[cur] in wh : raise LineParsingError('Expected whitespace after variable name', cur)
        return VariableName(vn),cur
    def get_parenthesis(t, i):
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
        return parse_expr(t[d:cur-1]),cur
    def get_number(t, i):
        cur = i
        comma = False
        if not t[cur] in n and not t[cur] == '.': return None
        a = t[cur]
        while cur < len(t)-1 and (t[cur+1] in n or t[cur+1] == '.'):
            if t[cur+1] == '.':
                if comma: 
                    raise LineParsingError("Not a number", cur)
                else:
                    comma = True
            cur+=1
            a+=t[cur]
        cur+=1
        if cur < len(t) and not t[cur] in wh : raise LineParsingError('Expected whitespace after number', cur)
        return Number(float(a)), cur
    cur = 0
    funcs = [get_string, get_variable_name, get_parenthesis, get_number]
    pile = []
    while cur < len(t):
        cur = skip_white_space(t, cur)
        for f in funcs:
            e = f (t, cur)
            if e != None:
                ep, cur = e
                pile.append(ep)
                break
        else:
            raise LineParsingError('Unexpected character: '+t[cur], cur)

    if len(pile) > 1 and not isinstance(pile[0], VariableName):
        raise LineParsingError('Calling a non callable')
    if len(pile) < 1:
        return None
    if len(pile) == 1:
        return pile[0]
    return Expr(pile[0], *pile[1:])
