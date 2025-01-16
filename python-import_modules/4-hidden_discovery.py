#!/usr/bin/python3
import marshal
import types

def get_defined_names(code):
    if isinstance(code, types.CodeType):
        for const in code.co_consts:
            if isinstance(const, types.CodeType):
                yield from get_defined_names(const)
        for name in code.co_names:
            yield name

def main():
    try:
        with open('/tmp/hidden_4.pyc', 'rb') as f:
            f.read(16)  # Skip the header
            code = marshal.load(f)
            names = list(get_defined_names(code))
            names.sort()
            for name in names:
                if not name.startswith('__'):
                    print(name)
    except FileNotFoundError:
        print("File not found: /tmp/hidden_4.pyc")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()