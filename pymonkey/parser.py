import pymonkey.ast as ast
import pymonkey.lexer as _lexer
import pymonkey.token as token
from typing import Optional


class Parser(object):
    lexer: _lexer
    cur_token: Optional[token.Token]
    peek_token: Optional[token.Token]

    def __init__(self, lexer: _lexer.Lexer):
        self.lexer = lexer
        self.cur_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def parse_program(self) -> Optional[ast.Program]:
        return None
