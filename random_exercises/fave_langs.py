# Ex 6-6 of Python Crash Course

fave_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

takeit = ("jen", "bill", "sanket", "edward", "kazu")

for name in takeit:
    if name in fave_langs.keys():
        print(f"Thanks for taking the poll, {name.title()}!")
    else:
        print(f"Take the poll, {name.title()}!")