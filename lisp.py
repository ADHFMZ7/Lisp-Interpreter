PROMPT = '*'


def read():
    try:
        return input(f'{PROMPT} ')
        
    except KeyboardInterrupt:
        print("\r* Exiting lisp\n")
        exit()



def evaluate(code):
    return code





def main():

    while 1:
        print(evaluate(read()))
    else:
        print("Exiting list")
        return


if __name__ == "__main__":
    main()
