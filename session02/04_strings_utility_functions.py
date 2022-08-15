sentence = "  This is a sentence.   "
stripped_sentence = sentence.strip()

print(sentence)
print(stripped_sentence)
print(stripped_sentence.upper())
print(stripped_sentence.lower())
print(stripped_sentence.find("sentence"))
print(stripped_sentence.replace("a sentence", "replaced"))

print(len(stripped_sentence))
