
print("=== Word Counter ===")

text = input("Enter a sentence: ")

words = text.split()
word_count = len(words)
character_count = len(text)
space_count = text.count(" ")

print("\n=== Result ===")
print("Total words:", word_count)
print("Total characters:", character_count)
print("Total spaces:", space_count)
