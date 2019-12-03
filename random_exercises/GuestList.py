# Guest list, from ex. 3-4 of Python Crash Course
guests = ["ronnie shellist", "leonardo da vinci", "benjamin franklin", "curt bartholomew"]

def invite():
    for x in guests:
        print(x.title() + ", you are hereby invited to the vegan extravaganza.")
    print(str(len(guests)) + " guests have been invited!")
invite()

absent = guests.pop() #Removes last element from guest list
print("Unfortunately, " + absent.title() + " cannot attend the dinner party.")
guests.append("Dagoberto Giraldo")

invite()

print("But wait, we have a table set for eight!")
guests.insert(0, "Bill Dause")
guests.append("Milton Pachon")
middle = len(guests)//2  #Finds the middle of the list, and drops the remainder
guests.insert(middle, "Shiney")
guests.insert(middle, "Ana Xielo")

invite()

print("Oh God! The table is on fire! Only two people can come.")
uninvited= []
while len(guests) > 2:       #Moves guests from guest list until two remain
    uninvited.append(guests.pop())

def uninvite():        #Uninvites guests
    for x in uninvited:
        print(x.title() + ", I'm so sorry. You cannot come. Our table burst into flames.")

uninvite()
invite()

del guests[0]
del guests[0]
print(guests)