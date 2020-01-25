# Copyright (C) 2020 Mohamed H
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

from minisoap.parser import (
    Parser,
    Sequence,
    Expr,
    Number,
    String,
    VariableName,
    Help,
    Transition
)
p = Parser()

parse_line = p.parse_line


def test_string():
    assert parse_line('""').__str__() == Sequence(String("")).__str__()


def test_number_1():
    assert parse_line('65').__str__() == Sequence(Number(65)).__str__()


def test_number_2():
    assert parse_line('65.7').__str__() == Sequence(Number(65.7)).__str__()


def test_number_3():
    assert parse_line('.5').__str__() == Sequence(Number(.5)).__str__()


def test_variable():
    assert parse_line('a$h\'o78').__str__() == Sequence(
        VariableName("a$h'o78")).__str__()


def test_parenthesis():
    assert parse_line('(a)').__str__() == Sequence(VariableName("a")).__str__()


def test_func_call():
    print(parse_line('print 0 1 abc').__str__())
    assert parse_line('print 0 1 abc').__str__() == \
        Sequence(Expr(VariableName('print'), Number(0),
                      Number(1), VariableName('abc'))).__str__()


def test_eq():
    assert parse_line('a=54').__str__() == Sequence(
        VariableName("a"), Number(54)).__str__()


def test_complex():
    s = parse_line('a\'=    \t     print       (sum          5 8) 4').__str__()
    assert s == Sequence(VariableName(
        "a'"
    ), Expr(
        VariableName('print'),
        Expr(
            VariableName('sum'),
            Number(5),
            Number(8)
        ),
        Number(4)
    )).__str__()


def test_helper():
    assert parse_line('open ?').__str__() == Help('open').__str__()


def test_void():
    assert parse_line('') is None


def test_comment1():
    assert parse_line('//lives') is None


def test_comment2():
    s = parse_line('a=5//lives').__str__()
    assert s == Sequence(VariableName("a"), Number(5)).__str__()


def test_transition_multiline():
    try:
        parse_line('{')
    except Exception as e:
        assert parse_line('}', e).__str__() == Sequence(
            Transition([])).__str__()


def test_transition():
    assert parse_line('{0s:1; 50ms: 0;;0.5s: 1;}').__str__() == Sequence(
        Transition([(0.0, 1.0), (0.05, 0.0), (0.5, 1.0)])).__str__()
