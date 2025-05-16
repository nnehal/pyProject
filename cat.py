import sys

def with_files(files):
    try:
        file_contents = [contents for contents in [open(file).read() for file in files]]
    except OSError as err:
        exit(print(f"cat: error reading files ({files})"))

    for contents in file_contents:
        sys.stdout.write(contents)

def no_files():
    try:
        while True:
            print(input())
    
    except KeyboardInterrupt:
        exit()
    except EOFError:
        exit()

def main():
    if not sys.argv[1:]:
        no_files()
    else:
        with_files(sys.argv[1:])

if __name__ == "__main__":
    main()