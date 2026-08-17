from collections import defaultdict


def init(words):
    wordsChar = {}
    for word in words:
        wordsChar[word] = list(word) + ["_"]


def countPairs(wordsChar: dict, wordFreq: dict) -> dict:
    pairs = defaultdict(int)
    for word, chars in wordsChar.items():
        freq = wordFreq[word]
        for i in range(len(chars) - 1):
            pair = (chars[i], chars[i + 1])
            pairs[pair] += freq
    return pairs


def mergePair(pair, wordsChar):
    a, b = pair
    merged = a + b
    for word, chars in wordsChar.items():
        i = 0
        new_chars = []
        while i < len(chars):
            if i < len(chars) - 1 and chars[i] == a and chars[i + 1] == b:
                new_chars.append(merged)
                i += 2
            else:
                new_chars.append(chars[i])
                i += 1
        wordsChar[word] = new_chars
    return wordsChar


def trainBPE(wordsChar, wordFreq, num_merges):
    merges = []
    for _ in range(num_merges):
        pairs = countPairs(wordsChar, wordFreq)
        if not pairs:
            break
        best_pair = max(pairs, key=lambda k: pairs[k])
        wordsChar = mergePair(best_pair, wordsChar)
        merges.append(best_pair)
    return wordsChar, merges


def tokenize(word, merges):
    chars = list(word) + ["_"]
    for a, b in merges:
        merged = a + b
        i = 0
        new_chars = []
        while i < len(chars):
            if i < len(chars) - 1 and chars[i] == a and chars[i + 1] == b:
                new_chars.append(merged)
                i += 2
            else:
                new_chars.append(chars[i])
                i += 1
        chars = new_chars
    return chars


wordFreq = {"low": 5, "lower": 2, "newest": 6, "widest": 3}
wordsChar = {word: list(word) + ["_"] for word in wordFreq}


trained = trainBPE(wordsChar, wordFreq, 100)

print(trained)
