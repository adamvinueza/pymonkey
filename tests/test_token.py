import pymonkey.token as token
from pymonkey.lexer import Lexer
import pytest_check as check


def test_next_token_semicolon():
    test_chars = "five;"
    tests = [
        token.Token(token.IDENT, 'five'),
        token.Token(token.SEMICOLON, ';')
    ]
    lxr = Lexer(test_chars)
    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type, f"expected {expected.type}, found {actual.type}")


def test_next_token_code():
    test_chars = \
        """
            let five = 5;
            let ten = 10;
            let add = fn(x, y) {
                x + y;
            };
            let result = add(five, ten);
        """
    tests = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    lxr = Lexer(test_chars)

    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type,
                    f"expected {expected.type}, found {actual.type}")


def test_next_token_basic():
    test_chars = '=+(){},;'

    tests = [
        token.Token(token.ASSIGN, '='),
        token.Token(token.PLUS, '+'),
        token.Token(token.LPAREN, '('),
        token.Token(token.RPAREN, ')'),
        token.Token(token.LBRACE, '{'),
        token.Token(token.RBRACE, '}'),
        token.Token(token.COMMA, ','),
        token.Token(token.SEMICOLON, ';'),
        token.Token(token.EOF, ''),
    ]

    lxr = Lexer(test_chars)

    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type,
                    f"expected {expected.type}, found {actual.type}")


def test_next_token_extended():
    test_chars = '''
        let five = 5;
        let ten = 10;
        let add = fn(x, y) {
            x + y;
        };
        let result = add(five, ten);
        !-/*5;
        5 < 10 > 5;
    '''

    tests = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.BANG, "!"),
        token.Token(token.MINUS, "-"),
        token.Token(token.SLASH, "/"),
        token.Token(token.ASTERISK, "*"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.GT, ">"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.EOF, ""),
    ]

    lxr = Lexer(test_chars)

    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type,
                    f"expected {expected.type}, found {actual.type}")


def test_next_token_keywords():
    test_chars = '''
        let five = 5;
        let ten = 10;
        let add = fn(x, y) {
            x + y;
        };
        let result = add(five, ten);
        !-/*5;
        5 < 10 > 5;
        
        if (5 < 10) {
            return true;
        } else {
            return false;
        }
    '''

    tests = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.BANG, "!"),
        token.Token(token.MINUS, "-"),
        token.Token(token.SLASH, "/"),
        token.Token(token.ASTERISK, "*"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.GT, ">"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.IF, "if"),
        token.Token(token.LPAREN, "("),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.TRUE, "true"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.ELSE, "else"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.FALSE, "false"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.EOF, token.EOF_CHAR),
    ]

    lxr = Lexer(test_chars)

    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type,
                    f"expected {expected.type}, found {actual.type}")


def test_next_token_peek():
    test_chars = '''
        let five = 5;
        let ten = 10;
        let add = fn(x, y) {
            x + y;
        };
        let result = add(five, ten);
        !-/*5;
        5 < 10 > 5;

        if (5 < 10) {
            return true;
        } else {
            return false;
        }
        10 == 10;
        10 != 9;
    '''

    tests = [
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "five"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "ten"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.INT, "10"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "add"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.FUNCTION, "fn"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "x"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "y"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.IDENT, "x"),
        token.Token(token.PLUS, "+"),
        token.Token(token.IDENT, "y"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.LET, "let"),
        token.Token(token.IDENT, "result"),
        token.Token(token.ASSIGN, "="),
        token.Token(token.IDENT, "add"),
        token.Token(token.LPAREN, "("),
        token.Token(token.IDENT, "five"),
        token.Token(token.COMMA, ","),
        token.Token(token.IDENT, "ten"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.BANG, "!"),
        token.Token(token.MINUS, "-"),
        token.Token(token.SLASH, "/"),
        token.Token(token.ASTERISK, "*"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.GT, ">"),
        token.Token(token.INT, "5"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.IF, "if"),
        token.Token(token.LPAREN, "("),
        token.Token(token.INT, "5"),
        token.Token(token.LT, "<"),
        token.Token(token.INT, "10"),
        token.Token(token.RPAREN, ")"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.TRUE, "true"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.ELSE, "else"),
        token.Token(token.LBRACE, "{"),
        token.Token(token.RETURN, "return"),
        token.Token(token.FALSE, "false"),
        token.Token(token.SEMICOLON, ";"),
        token.Token(token.RBRACE, "}"),
        token.Token(token.INT, '10'),
        token.Token(token.EQ, '=='),
        token.Token(token.INT, '10'),
        token.Token(token.SEMICOLON, ';'),
        token.Token(token.INT, '10'),
        token.Token(token.NOT_EQ, '!='),
        token.Token(token.INT, '9'),
        token.Token(token.SEMICOLON, ';'),
        token.Token(token.EOF, ""),
    ]

    lxr = Lexer(test_chars)

    for expected in tests:
        actual = lxr.next_token()
        check.equal(expected.type, actual.type,
                    f"expected {expected.type}, found {actual.type}")

