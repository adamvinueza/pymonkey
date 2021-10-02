import pymonkey.lexer as lexer
import pymonkey.ast as ast
import pymonkey.token as token
import pymonkey.parser as parser
import pytest_check as check


def test_let_statement():
    test_program = """
        let x = 5;
        let y = 10;
        let foobar = 838383;
    """
    lxr = lexer.Lexer(test_program)
    p = parser.Parser(lxr)
    program = p.parse_program()
    check.is_not_none(program, "parse_program returned None")
    expected_statements = 3
    actual_statements = len(program.statements)
    check.equal(expected_statements,
                actual_statements,
                f"expected {expected_statements} statements, found "
                f"{actual_statements}")
