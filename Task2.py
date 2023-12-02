id_no = []
value = []
hsh_ky = []

with open('wordsHK3.txt', 'r') as text_file:
    next(text_file)
    lines = text_file.readlines()
    for line in lines:
        data = line.strip().split('|')
        id_no.append(int(data[1].strip()))
        if data[2].strip() != 'Word':
            value.append(data[2].strip())
        if data[1].strip().isdigit():
            hsh_ky.append(int(data[3].strip()))

class hashKeyTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def __str__(self):
        return str(self.table)

    def put(self, hsh_key, value) -> object:
        level = 1
        hashCode = self.hash(hsh_key, level)
        new_Hash_key = hashCode % self.size
        while self.table[new_Hash_key] is not None:
            level += 1
            new_Hash_key = self.hash(hsh_key, level) % self.size
        if self.table[new_Hash_key] == value or self.table[new_Hash_key] is None:
            self.table[new_Hash_key] = value

            return hashCode, new_Hash_key

    def hash(self, value, i):
        c1 = 1
        c2 = 1
        c3 = 0
        hashCode = value + c1 * i * i + c2 * i + c3
        return hashCode


a = 0
b = 0
hash = hashKeyTable(163)
with open('wordsQHK3.txt', 'w') as textfile:
    textfile.write("| {:<20} | {:<20} | {:<20} | {:<20} | {:<20} |\n".format("Word_index", "Word", "Hash_Key", "new_Hash_key", "Quadratic h-f"))
    textfile.write("___________________________________________________________________________________________________________________\n")
    for i in range(len(value)):
        a,b = hash.put(hsh_ky[i], value[i])
        textfile.write("| {:<20} | {:<20} | {:<20} | {:<20} | {:<20} |\n".format(id_no[i], value[i], hsh_ky[i], a, b))