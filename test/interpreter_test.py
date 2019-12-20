from minisoap import Interpreter, parse_line
# TODO add more tests

def test_variable_assign():
    interpreter = Interpreter()
    interpreter.run(parse_line('a=5'))
    assert interpreter.run_expr(parse_line('a').expr) == 5.0
