from minisoap.parser import parse_line, Sequence, Expr, Number, String, VariableName, Help

def test_string():
    assert parse_line('""').__str__() == Sequence(String("")).__str__()

def test_number_1():
    assert parse_line('65').__str__() == Sequence(Number(65)).__str__()

def test_number_2():
    assert parse_line('65.7').__str__() == Sequence(Number(65.7)).__str__()

def test_number_3():
    assert parse_line('.5').__str__() == Sequence(Number(.5)).__str__()

def test_variable():
    assert parse_line('a$h\'o78').__str__() == Sequence(VariableName("a$h'o78")).__str__()

def test_parenthesis():
    assert parse_line('(a)').__str__() == Sequence(VariableName("a")).__str__()

def test_func_call():
    print(parse_line('print 0 1 abc').__str__())
    assert parse_line('print 0 1 abc').__str__() == \
        Sequence(Expr(VariableName('print'), Number(0), Number(1), VariableName('abc'))).__str__()

def test_eq():
    assert parse_line('a=54').__str__() == Sequence(VariableName("a"), Number(54)).__str__()

def test_complex():
    assert parse_line('a\'=     \t     print       (sum          5 8) 4').__str__() == Sequence(VariableName("a'"), Expr(VariableName('print'), Expr(VariableName('sum'), Number(5), Number(8)), Number(4))).__str__()

def test_helper():
    assert parse_line('open ?').__str__() == Help('open').__str__()