from enum import Enum

PROMPT = '*'


#==============================================================================

# R E P L 

def read(): 
    """
    Read lisp code from stdin and returns it as a string.
    """

    try:
        return input(f'{PROMPT} ').upper()
        
    except KeyboardInterrupt:
        print("\r* Exiting lisp\n")
        exit()

def evaluate(code): 
    """
    Takes in stream of code and evaluates it, returning the final value

    Code -> Tokenize -> Eval Tokens -> return final value

    ex) "(+ 1 2)" -> 3
    """

    tokens = tokenize(code) 

    return token_eval(tokens)

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

"(+ 2 (- (* 2 2) 4))"
"1"

def tokenize(code):
    """
    Takes stream of code and returns list of tokens

    tokens are of the following form
    Token:
        type
        value

    ex) "(+ 1 2)" -> 
    Token(List, (Token(Atom, add), Token(Atom, 1), Token(Atom, 2)))
    """
    

    def traverse(start):
        inner_tokens = []
        #value = 0 

        for ix, char in enumerate(code[start:]):

            if char == '(':
                inner_tokens.append(traverse(start + ix + 1))
            elif is_atom(char):
                inner_tokens.append(Token(Type.ATOM, char))
            elif char == ')':
                return Token(Type.LIST, inner_tokens)
            elif char.isspace():
                continue
            else:
                error(f"Unrecognized symbol {char}")
        return inner_tokens

    return traverse(0)

    # counter = 0
    # for char in code:
    #     if char == '(':
    #         counter += 1
    #     elif char == ')':
    #         counter -= 1
    #     elif char == '':
    # 
    # if counter:
    #
    #
    #
    # return tokens

def token_eval(tokens):
    print(tokens)
    # for token in tokens:
    #     if token.ltype == "list": # TODO: CHANGE TO ENUM LATER
    #         #if token.value[0] is a function evaluate list and return
    #
    #         token.value = token_eval(token.value)  # Overwrites value. See if this is doable, or another attribute is needed
    

def is_atom(symbol):
    return not symbol.isspace() 

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


