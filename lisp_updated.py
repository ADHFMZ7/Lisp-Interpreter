import sys
from enum import Enum

# class token_types(Enum):
#     integer,
#     float,
#     string,
#     list

def tokenize(buffer):

    index = 0 
    offset = 1
    

    while index < len(buffer):

        slice = buffer[index:index + offset]

        if buffer[index] == " ":
            index += 1

        elif slice == '"':
            offset = 1

            while buffer[index + offset] != '"':
                offset += 1
            print(buffer[index: index+offset+1])
            index += offset + 1
            offset = 1

        elif not slice in ['(', ')', 'int', 'main', '{', '}', 'printf', ';']:
            offset += 1
        else:
            index += offset 
            offset = 1
            print(slice)

def main():
    tokenize('int main()\n{\nprintf("Hello world");\n}'.replace('\n', ''))


if __name__ == "__main__":
    main()
