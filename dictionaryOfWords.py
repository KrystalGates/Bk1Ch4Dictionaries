# """
# Create a dictionary with key value pairs to
# represent words (key) and its definition (value)
# """
word_definitions = dict()
print(word_definitions)

# """
# Add several more words and their definitions
#    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
# """
word_definitions["crick"] = "A common Southernism refering to a pain, spasm, or strain in a joint such as a neck, back, or knee."

word_definitions["number neighbor"] = "Someone who has the same phone number as you, besides the last digit."

word_definitions["prime timing"] = "Staying up late watching TV after midnight. Usually primetiming involves watching reruns of favorite shows."

# """
# Use square bracket lookup to get the definition of two
# words and output them to the console with `print()`
# """
print("crick:", word_definitions["crick"], "primetiming:", word_definitions["prime timing"])


# """
# Loop over the dictionary to get the following output:
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
# """
# for key,value in my_pairs.items():
#     print(f"This came from my_pairs: {value}")

for word,definition in word_definitions.items():
    print(f"The definition of {word} is {definition}.")