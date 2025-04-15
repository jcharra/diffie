from collections import defaultdict

# Load the word list (assume one word per line)
with open("de_50k.txt", encoding='utf-8') as f:
    words = [line.split()[0].strip().lower() for line in f if len(line.strip()) > 1]

# Group words by length to make comparisons faster
length_groups = defaultdict(list)
for word in words:
    length_groups[len(word)].append(word)

# Function to count differences
def one_letter_diff(w1, w2):
    return sum(c1 != c2 for c1, c2 in zip(w1, w2)) == 1

# Store pairs
pairs = set()

# Compare words in each length group
for length, group in length_groups.items():
    if length not in [4, 5, 6]:
      continue
    print(f"Searching for length {length} (words: {len(group)})")
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            w1, w2 = group[i], group[j]
            if one_letter_diff(w1, w2):
                pairs.add(tuple(sorted((w1, w2))))

with open("pairs.txt", "w") as out:
    for a, b in pairs:
        out.write(a + " " + b + "\n")