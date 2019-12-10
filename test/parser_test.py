from minisoap.parser import parse_line, Sequence, Expr, Number, String, VariableName

def test_string():
    assert parse_line('""').__str__() == Sequence(String("")).__str__()

def test_number_1():
    assert parse_line('65').__str__() == Sequence(Number(65.0)).__str__()

def test_number_2():
    assert parse_line('65.7').__str__() == Sequence(Number(65.7)).__str__()

def test_number_3():
    assert parse_line('.5').__str__() == Sequence(Number(.5)).__str__()

def test_variable():
    assert parse_line('a$h\'o78').__str__() == Sequence(VariableName("a$h'o78")).__str__()

def test_parenthesis():
    assert parse_line('(a)').__str__() == Sequence(VariableName("a")).__str__()
