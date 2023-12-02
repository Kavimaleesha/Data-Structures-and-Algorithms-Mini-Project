def compute_hsh_ky(wrds):
    # English alphabet's letters and their numbers
    english_alphabet = [x for x in range(52)]
    for x in range(26):
        english_alphabet[x] = x
        english_alphabet[x + 26] = x + 26

    hsh_ky = 0

    # Compute the current word's hash key.
    for b in wrds:
        char_value = -1
        if 'a' <= b <= 'z':
            char_value = ord(b) - ord('a')
        elif 'A' <= b <= 'Z':
            char_value = ord(b) - ord('A') + 26
        if char_value != -1:
            hsh_ky += english_alphabet[char_value]
        else:
            return None
    return hsh_ky


def main():

    # Open the input and output files
    with open("file3.txt", "r") as textfile:
        words = textfile.read().split()

    seen_words = set()
    hsh_kys = []
    id = 1

    with open("wordsHK3.txt", "w") as textfile:
        # Print table header
        textfile.write("| {:<5}| {:<20}| {:<10}|\n".format("Index", "Word", "Hash Key"))

        for word in words:
            # Finding that the word being used has not already been processed
            if word in seen_words:
                continue
            seen_words.add(word)

            hsh_ky = compute_hsh_ky(word)
            if hsh_ky is not None:
                # Add the hash key to the existing list
                hsh_kys.append(hsh_ky)

                # To the output file, add the word and the hash key.
                textfile.write("| {:<5}| {:<20}| {:<10}|\n".format(id, word, hsh_ky))
                id += 1

    print("Hashing completed successfully.")
if __name__ == "__main__":
    main()