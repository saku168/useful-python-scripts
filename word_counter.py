"""Count words, characters and lines in text entered by the user."""
def main():
    print("Paste text below. Submit an empty line to finish:")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        lines.append(line)
    text = "\n".join(lines)
    print("\n--- Text statistics ---")
    print(f"Words: {len(text.split())}")
    print(f"Characters: {len(text)}")
    print(f"Characters without whitespace: {len(''.join(text.split()))}")
    print(f"Lines: {len(lines)}")

if __name__ == "__main__":
    main()
