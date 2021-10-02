import string
from pymonkey.token import Token
import pymonkey.token as token


class Lexer(object):
    def __init__(self, tokens: str):
        self.tokens = tokens
        self.position = 0
        self.read_position = 0
        self.char = token.EOF_CHAR
        self.read_char()

    def read_char(self):
        if self.read_position >= len(self.tokens):
            self.char = token.EOF_CHAR
        else:
            self.char = self.tokens[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def skip_whitespace(self):
        while self.char in string.whitespace:
            self.read_char()

    @staticmethod
    def is_letter(ch):
        return 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'

    def read_identifier(self):
        position = self.position
        while Lexer.is_letter(self.char):
            self.read_char()
        return self.tokens[position:self.position]

    def read_number(self):
        position = self.position
        while str.isdigit(self.char):
            self.read_char()
        return self.tokens[position:self.position]

    def peek_char(self) -> str:
        if self.read_position >= len(self.tokens):
            return token.EOF_CHAR
        return self.tokens[self.read_position]

    def peek_for_token(self, ch, check_tok, yes_tok, no_tok):
        """Peek at the next character and if it matches the check token,
        return the "yes" token, otherwise return the "no" token."""
        if self.peek_char() == check_tok:
            first = ch
            self.read_char()
            literal = first + self.char
            return Token(yes_tok, first + self.char)
        else:
            return Token(no_tok, ch)

    def get_non_identifier_token(self) -> Token:
        ch = self.char
        match ch:
            case token.ASSIGN:
                tok = self.peek_for_token(ch, token.ASSIGN, token.EQ, token.ASSIGN)
            case token.BANG:
                tok = self.peek_for_token(ch, token.ASSIGN, token.NOT_EQ, token.BANG)
            case token.ASTERISK:
                tok = Token(token.ASTERISK, ch)
            case token.COMMA:
                tok = Token(token.COMMA, ch)
            case token.GT:
                tok = Token(token.GT, ch)
            case token.LBRACE:
                tok = Token(token.LBRACE, ch)
            case token.LPAREN:
                tok = Token(token.LPAREN, ch)
            case token.LT:
                tok = Token(token.LT, ch)
            case token.MINUS:
                tok = Token(token.MINUS, ch)
            case token.PLUS:
                tok = Token(token.PLUS, ch)
            case token.RBRACE:
                tok = Token(token.RBRACE, ch)
            case token.RPAREN:
                tok = Token(token.RPAREN, ch)
            case token.SEMICOLON:
                tok = Token(token.SEMICOLON, ch)
            case token.SLASH:
                tok = Token(token.SLASH, ch)
            case token.EOF_CHAR:
                tok = Token(token.EOF, ch)
            case _:
                tok = Token(token.ILLEGAL, ch)
        return tok

    def next_token(self) -> Token:
        self.skip_whitespace()
        ch = self.char
        if Lexer.is_letter(ch):
            literal = self.read_identifier()
            tok = Token(token.lookup_ident(literal), literal)
        elif str.isdigit(ch):
            literal = self.read_number()
            tok = Token(token.INT, literal)
        else:
            tok = self.get_non_identifier_token()
            self.read_char()
        return tok
