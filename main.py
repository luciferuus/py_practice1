import math


def inputs_get() -> tuple:
    a = num_read("Input A")
    b = num_read("Input B")
    x = num_read("Input X")
    return a, b, x


def num_read(msg):
    while True:
        try:
            print("{0}:".format(msg))
            num = float(input())
            return num
        except ValueError:
            print("ERROR:Value_error")
            print("Please try again.")


def calculate(a, b, x):
    return (1 / (2 * b)) * math.pow(math.e, (-1 * math.fabs(x - a)) / b)


def main():
    inputs = inputs_get()
    print("Result of calculations:")
    print(calculate(*inputs))


if __name__ == '__main__':
    main()
