import random
with open("words.txt","r")as f:
    content = f.read()
    words = list(content.split())
word=random.choice(words)
def print_ouput():
    output="".join(dash)
    print(output)
print(f"I am a {len(word)} letter word,guess me!")
dash=["_" ]*len(word)
print_ouput()

#loop to take the guesses
for i in range(8):
    if "_" not in dash:
        break
    letter = input("Guess a letter: ")
    if letter in word:
        for x, i in enumerate(word):
            if letter == i:
                dash[x] = letter
    else:
        print(f"Incorrect guess,try again")
    print_ouput()
if "_" not in dash:
    print("Hurray you won")
else:
    print("sorry,you lost!try again")
