# Ex 6-1, 6-7 Python Crash Course

people = {
    'bswin' : {
        'first_name' : 'Brandon', 
        'last_name' : 'Swinford', 
        'city' : 'Franklin',
        },
    'hstev' : {
        'first_name' : 'Haley', 
        'last_name' : 'Stevens', 
        'city' : 'Jupiter',
    },
    'mbuen' : {
        'first_name' : 'Mark', 
        'last_name' : 'Buente', 
        'city' : 'Washington, D.C.',
    }}

for person, info in people.items():
    full_name = info['first_name'] + " " + info['last_name']
    print(f"{full_name} lives in {info['city']}.")






