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
    print(tokens)
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
    
    expr = Token(Type.EXPR, None)

    def traverse(start):
        inner_tokens = []
        getting_atom = False
        inside = False
        opened = code[start-1] == '(' if start > 0 else False

        for ix, char in enumerate(code[start:]):
            if char == '(':
                opened = True
                if start + ix == 0:
                    continue
                inner_tokens.append(traverse(start + ix + 1))
                inside = 1
            elif char == ')' :
                if not opened:
                    error("Unmatched parenthesis; '(' missing.")
                if inside:
                    inside = False 
                    continue
                return Token(Type.LIST, inner_tokens)
            elif is_atom(char):
                if getting_atom or inside:
                    continue
                inner_tokens.append(get_atom(code, start + ix))
                getting_atom = True

            elif char.isspace():
                if getting_atom:
                    getting_atom = False

            else:
                error(f"Unrecognized symbol {char}.")
        if opened:
            error("Unmatched parenthesis; ')' missing.")
        return inner_tokens if inner_tokens else  None
   
    expr.value = traverse(0) 
    return expr

def token_eval(token):
    if token.t_type == Type.EXPR:
        pass
    if token.t_type == Type.ATOM:
        pass 





    if token.t_type == Type.LIST:
        pass
    # for token in tokens:
    #     if token.ltype == "list": # TODO: CHANGE TO ENUM LATER
    #         #if token.value[0] is a function evaluate list and return
    #
    #         token.value = token_eval(token.value)  # Overwrites value. See if this is doable, or another attribute is needed
    return 99

def get_atom(string, ix):
    return Token(Type.ATOM, string[ix:].split()[0])

def is_atom(symbol):
    return (not symbol.isspace() ) and (symbol not in "()")

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


