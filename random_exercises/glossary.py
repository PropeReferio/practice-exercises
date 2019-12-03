# Ex 6-3 Python Crash Course

glossary = {
    'Python' : 'A language invented by the Dutch in the \'80s.',
    'Loops' : 'A powerful type of code that allows you to work with many items in a list, dictionary, or tuple.',
    'Program' : 'A simple document which, when interpreted by a specific language, can acheive the programmer\'s intentions.',
    'Language' : 'A set of commands, functions, and syntax that a programmer must master to acheive their ends.',
    'Data Type' : 'Different kinds of information, such as lists, integers, floats, and strings.'
    }


for word, defin in glossary.items():
    print("\n" + word + ":")
    print("\t " + defin)
