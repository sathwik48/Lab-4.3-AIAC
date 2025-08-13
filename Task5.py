def analyze_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
        first_line = lines[0].strip() if lines else ''
    return num_lines, num_words, num_chars, first_line

if __name__ == "__main__":
    file_path = input("Enter the path to the .txt file: ")
    try:
        lines, words, chars, first = analyze_text_file(file_path)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {chars}")
        print(f"First line: {first}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")