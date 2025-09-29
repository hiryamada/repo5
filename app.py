import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python app.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide two numbers.")
        sys.exit(1)
    result = add(num1, num2)
    print(result)