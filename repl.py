#!/usr/bin/env python
import os
import pwd
from pymonkey.lexer import Lexer
import pymonkey.token as token

PROMPT = ">> "


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def start():
    while True:
        print(PROMPT, end='')
        line = input()
        if not line:
            print("bye!")
            return
        lxr = Lexer(line)
        tok = lxr.next_token()
        while tok.type != token.EOF:
            print(tok)
            tok = lxr.next_token()


def run():
    user = get_username()
    print(f"Hello {user}! This is the Monkey programming language!\n")
    print("Feel free to type in commands")
    print("Type ENTER at the prompt to quit")
    start()


if __name__ == '__main__':
    run()
