from functools import reduce
from enum import Enum
import re

PROMPT = '*'
PATTERN = r"[\s,]*(~@|[\[\]{}()'`~^@]|\"(?:\\.|[^\\\"])*\"?|;.*|[^\s\[\]{}('\"`,;)]*)"

env = {


    # Arithmetic operators
    '+' : lambda *args : sum(args),
    '-' : lambda a, *b : a - sum(b),
    '*' : lambda *args : reduce(lambda a, b: a*b, args),
    '/' : lambda a, *b : a // reduce(lambda x, y: x*y, b),

    'EXIT': lambda : exit(0)
}

#==============================================================================

# R E P L 

def read(prompt=PROMPT): 
    """
    Read lisp code from stdin and returns it as a list of tokens.
    """

    try:
        lines = []
        while True:
            line = input(f'{prompt} ')
            lines.append(line)

            # Check if the current line is the end of a multiline expression
            if sum([i.count('(') - i.count(')') for i in lines]) > 0:
                #prompt = '    '  # Use an increased indentation for the next line
                #Will try to make auto indent work at another point.
                prompt = ' '
            else:
                break  # Exit the loop if the current line is the last line of the expression

        return re.findall(PATTERN, '\n'.join(lines).upper())

    except KeyboardInterrupt:
        print("\r* Exiting lisp\n")
        exit()


def evaluate(tokens): 
    """
    Takes in stream of tokens and evaluates it, returning the final value

    Tokenizs -> Eval Tokens recursively -> return final value

    ex) "(+ 1 2)" -> 3
    """

    return token_eval(tokenize(tokens))

#==============================================================================

# Token Class

class Type(Enum):
    LIST = 1
    ATOM = 2
    EXPR = 4

class Token:
    def __init__(self, t_type: Type, value):
        self.t_type = t_type 
        self.value = value

    def __repr__(self):
        return f"Token({self.t_type}, {self.value})"

#==============================================================================

# Helper Functions 


def tokenize(tokens):
    """
    Takes stream of code and returns list of tokens

    tokens are of the following form
    Token:
        type
        value

    ex) "(+ 1 2)" -> 
    Token(List, (Token(Atom, add), Token(Atom, 1), Token(Atom, 2)))
    """
    expr = Token(Type.EXPR, None)

    def traverse(start):
        inner_tokens = []
        inside = False
        opened = tokens[start-1] == '(' if start > 0 else False

        for ix, tok in enumerate(tokens[start:]):
            if tok == '(':
                opened = True
                if start + ix == 0:
                    continue
                inner_tokens.append(traverse(start + ix + 1))
                inside = 1
            elif tok == ')' :
                if not opened:
                    error("Unmatched parenthesis; '(' missing.")
                if inside:
                    inside = False 
                    continue
                return Token(Type.LIST, inner_tokens)
            else:
                if inside:
                    continue
                inner_tokens.append(build_atom(tok))
        if opened:
            error("Unmatched parenthesis; ')' missing.")
        return inner_tokens if inner_tokens else  None
   
    expr.value = traverse(0) 
    return expr


def token_eval(token):

    token_val = token.value[0] if isinstance(token.value, list) else token.value

    if token.t_type == Type.EXPR:

        return token_eval(token_val)
    elif token.t_type == Type.ATOM:
        try:
            return int(token_val)
        except:
            #error("DIDNT WORK")
            pass
        try:
            return env[token_val]
        except:
            error(f"Undefined symbol {token_val}")
        
    elif token.t_type == Type.LIST:
        try:
             
            argv = [token_eval(tok) for tok in token.value]
            argc = len(argv)
            return argv[0](*argv[1:])
        except:
            error(f"Failed to run function '{token.value[0].value}'")


    return 99
def build_atom(token):
    return Token(Type.ATOM, token)

def error(message):
    print(f"\033[31;1;4mERROR\033[0m: {message}")
    exit(1)

def main():

    while 1:
        print(evaluate(read()))
    else:
        print("Exiting lisp")
        return


if __name__ == "__main__":
    main()


