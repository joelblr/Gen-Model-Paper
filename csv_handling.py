def get_csv_line_offsets(filename: str) -> list[int]:
    offsets: list[int] = []
    with open(filename, 'r', newline='', encoding='utf-8') as file :
        offset: int = 0
        for line in file :
            offsets.append(offset)
            offset += len(line.encode('utf-8'))  # Byte offset
    return offsets


def read_specific_csv_lines(filename: str, line_indices: list[int]) -> list[list[str]]:

    offsets: list[int] = get_csv_line_offsets(filename)
    lines: list[list[str]] = []

    with open(filename, 'r', newline='', encoding='utf-8') as file:
        for index in line_indices :
            file.seek(offsets[index])
            lines.append(file.readline().strip().split(','))  # Split CSV row
    return lines

if __name__ == "__main__" :

    # Example usage for specific lines
    print("Running csv_handling.py")
    line_indices: list[int] = [10,30,50]  # Example line indices
    specific_lines = read_specific_csv_lines('main.py', line_indices)
    for line in specific_lines :
        print(line)
