TokenType = str
EOF_CHAR = chr(0)


class Token(object):
    def __init__(self, token_type: TokenType, literal: str):
        self.type = token_type
        self.literal = literal

    def __str__(self):
        return f"{{Type:{self.type} Literal:{self.literal}}}"


def lookup_ident(ident) -> TokenType:
    try:
        return keywords[ident]
    except KeyError:
        return IDENT


'''
Constants
'''

ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers and literals
IDENT = "IDENT" # add, foobar, x, y, ...
INT = "INT"

# Operators
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"

LT = "<"
GT = ">"

EQ = "=="
NOT_EQ = "!="

# Delimiters
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"

keywords = {
    'fn': FUNCTION,
    'let': LET,
    'true': TRUE,
    'false': FALSE,
    'if': IF,
    'else': ELSE,
    'return': RETURN,
}
