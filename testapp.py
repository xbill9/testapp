def generate_fibonacci(count):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(count):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers.")
    parser.add_argument(
        "count", type=int, help="The number of Fibonacci numbers to generate."
    )
    args = parser.parse_args()

    if args.count < 0:
        print("Please provide a non-negative integer for the count.")
    else:
        fib_numbers = generate_fibonacci(args.count)
        print(f"Fibonacci sequence up to {args.count} numbers: {fib_numbers}")
