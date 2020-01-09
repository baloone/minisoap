from minisoap import Interpreter, Parser
# TODO add more tests
p = Parser()

parse_line = p.parse_line

def test_variable_assign():
    interpreter = Interpreter()
    interpreter.run(parse_line('a=5'))
    assert interpreter.run_expr(parse_line('a').expr) == 5.0
