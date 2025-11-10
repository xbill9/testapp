from typing import List


def generate_lucas(count: int) -> List[int]:
    """Generates a Lucas sequence up to a given count."""
    lucas_sequence = []
    a, b = 2, 1
    for _ in range(count):
        lucas_sequence.append(a)
        a, b = b, a + b
    return lucas_sequence


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Lucas numbers.")
    parser.add_argument(
        "count", type=int, help="The number of Lucas numbers to generate."
    )
    args = parser.parse_args()

    if args.count < 0:
        print("Please provide a non-negative integer for the count.")
    else:
        lucas_numbers = generate_lucas(args.count)
        print(f"Lucas sequence up to {args.count} numbers: {lucas_numbers}")
