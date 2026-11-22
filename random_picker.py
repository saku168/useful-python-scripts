"""Pick a random item from a comma-separated list."""
import random

def main():
    choices = [item.strip() for item in input("Choices (separated by commas): ").split(",")]
    choices = [item for item in choices if item]
    if choices:
        print("Selected:", random.choice(choices))
    else:
        print("Please enter at least one choice.")

if __name__ == "__main__":
    main()
