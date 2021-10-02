from typing import List, Protocol
import pymonkey.token as _token


class Node(Protocol):
    def token_literal(self) -> str:
        return ''


class Statement(Node, Protocol):
    def statement_node(self):
        pass


class Expression(Node, Protocol):
    def expression_node(self):
        pass


class Program(Node):
    statements: List[Statement]

    def __init__(self, statements: List[Statement]):
        self.statements = statements

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        else:
            return ''


class Identifier(Expression):
    token: _token.Token
    value: str

    def __init__(self, token: _token.Token, value: str):
        self.token = token
        self.value = value

    def expression_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal


class LetStatement(Statement):
    token: _token.Token
    name: Identifier
    value: Expression

    def statement_node(self):
        pass

    def token_literal(self) -> str:
        return self.token.literal
