# Write your code here.
#Task 1

def hello():
    return "Hello!"

#Task 2
def greet(name):
    return f"Hello, {name}!"


# Task 3

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b

        elif operation == "subtract":
            return a - b

        elif operation == "multiply":
            return a * b

        elif operation == "divide":
            return a / b

        elif operation == "modulo":
            return a % b

        elif operation == "int_divide":
            return a // b

        elif operation == "power":
            return a ** b

    except ZeroDivisionError:
        return "You can't divide by 0!"

    except TypeError:
        return f"You can't {operation} those values!"
    

    #Task 4
def data_type_conversion(value,type):
    try:
        if type == "int":
            return int(value)
        elif type == "float":
             return float(value)
        elif type == "str":
                return str(value)
            
    except ValueError:
            return f"You can't convert {value} into a {type}."
#Task 5


def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    except TypeError:
        return "Invalid data was provided."


#Task 6
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string

    return result 


# Task 7

def student_scores(type, **kwargs):
    if type == "best":
        best = ""
        highest_score = 0

        for key, value in kwargs.items():
            if value > highest_score:
                highest_score = value
                best = key

        return best

    elif type == "mean":
        return sum(kwargs.values()) / len(kwargs)
    
# Task 8

def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    words = string.split()
    title_words = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            title_words.append(word.capitalize())

        elif word in little_words:
            title_words.append(word)

        else:
            title_words.append(word.capitalize())

    return " ".join(title_words)

#Task 9

def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result

# Task 10
# Task 10

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        consonants = ""
        rest = word

        while len(rest) > 0 and rest[0] not in vowels:
            # handle qu together
            if rest.startswith("qu"):
                consonants += "qu"
                rest = rest[2:]
                break
            else:
                consonants += rest[0]
                rest = rest[1:]

        if consonants == "":
            result.append(word + "ay")
        else:
            result.append(rest + consonants + "ay")

    return " ".join(result)



print(hello())
print(greet("Mak"))
print(calc(3,4, "add"))
print(calc(3,0, "divide"))
print(calc("Hi", "Mam", "multiply"))
print(data_type_conversion("15", "int"))
print(data_type_conversion("nonsense", "float"))
print(grade(45,95,100))
print(grade("hello",90))
print(repeat("wow", 3))
print(student_scores("best", Rahul=90, Yovan=95, Marry=85))
print(student_scores("mean", Rahul=90, Yovan=95, Marry=85))
print(titleize("the hidden temple in the village"))
print(hangman("codethedream","dr"))
print(pig_latin("apple"))
print(pig_latin("cherry"))
print(pig_latin("orange"))