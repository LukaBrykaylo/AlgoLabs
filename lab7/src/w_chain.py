def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        number = lines[0].strip()
        words = [word.strip() for word in lines[1:]]

    return number, words


def longest_chain():
    number, words = read_file("lab7\src\wchain.in")
    if number == 0:
        return

    words.sort(key=len)
    saved_results = [1] * len(words)

    for i in range(len(words)):
        for next_word in range(i):
            if is_word2_has_word1(words[next_word], words[i]):
                saved_results[i] = max(
                    saved_results[i], saved_results[next_word] + 1)

    write_file("lab7\src\wchain.out", max(saved_results))

    return max(saved_results)


def is_word2_has_word1(word1, word2):
    n, m = len(word1), len(word2)
    i = j = 0

    while i < n and j < m:
        if word1[i] == word2[j]:
            i += 1
        j += 1
    if i - m > 1 or j - n > 1:
        return False

    return i == n


def write_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))
