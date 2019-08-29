# Instructions
# 1. Define a dictionary that contains information about several members of your family. Use the following example as a template.

# my_family = {
#     "sister": {
#         "name": "Krista",
#         "age": 42
#     },
#     "mother": {
#         "name": "Cathie",
#         "age": 70
#     }
# }

my_family = {
    "sister": {
        "name": "Sheri",
        "age": 25
    },
    "mother": {
        "name": "Juliann",
        "age": 55
    },
    "father": {
        "name": "Ronald",
        "age": 73
    }
}
# 2. Using a dictionary comprehension, produce output that looks like the following example.

for key, value in my_family.items():
    print(f'{value["name"]} is my {key} and is {str(value["age"])} years old')


# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)