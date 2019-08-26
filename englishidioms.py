# Create a new Python file and paste the following code into it. At the end write a for in loop to produce the output below.

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}
# Make sure you join the strings

for key,value in idioms.items():
    space = " "
    sentence = space.join(value)
    print(f'{key}: {sentence}')

# Output
# Penny: A penny for your thoughts
# Injury: Add insult to injury
# Moon: Once in a blue moon
# Grape: I heard it through the grapevine
# Murder: Kill two birds with one stone
# Limbs: It costs an arm and a leg
# Grain: Take what someone says with a grain of salt
# Fences: I'm on the fence about it
# Sheep: Pulled the wool over his eyes
# Lucifer: Speak of the devil