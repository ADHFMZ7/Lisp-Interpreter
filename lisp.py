PROMPT = '*'


def read():
    try:
        return input(f'{PROMPT} ').upper()
        
    except KeyboardInterrupt:
        print("\r* Exiting lisp\n")
        exit()

def evaluate(code): # assume code is a full lisp expression
    """
    Takes in stream of code and evaluates it, returning
    the final value

    ex) "(+ 1 2)" -> 3
    """


    tokens = tokenize(code) 

    token_eval(tokens)





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

    tokens = []

    return tokens

def token_eval(tokens):
    for token in tokens:
        if token.ltype == "list": # TODO: CHANGE TO ENUM LATER
            # if token.value[0] is a function evaluate list and return

            token.value = token_eval(token.value)  # Overwrites value. See if this is doable, or another attribute is needed
        

def main():

    while 1:
        print(evaluate(read()))
    else:
        print("Exiting lisp")
        return


if __name__ == "__main__":
    main()
