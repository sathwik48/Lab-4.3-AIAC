def analyze_text_file(filename):
    """
    Reads a .txt file and returns:
    - number of lines
    - number of words
    - number of characters
    - the first line
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
            first_line = lines[0].rstrip('\n') if lines else ""
        return num_lines, num_words, num_chars, first_line
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None, None, None, None

if __name__ == "__main__":
    filename = input("Enter the path to the .txt file: ")
    num_lines, num_words, num_chars, first_line = analyze_text_file(filename)
    if num_lines is not None:
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
        print(f"First line: {first_line}")
