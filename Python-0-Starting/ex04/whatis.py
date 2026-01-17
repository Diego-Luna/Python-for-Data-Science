import sys

def main():
    # * Check if more than one argument is provided
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    
    # ! If no argument, exit silently
    if len(sys.argv) < 2:
        return
    
    # * Try to convert argument to integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    # * Check if even or odd
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
