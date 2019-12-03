#Python Crash Course 8-7. Album: Write a function called make_album() that 
#builds a dictionary describing a music album . The function should take in 
# an artist name and an album title, and it should return a dictionary 
# containing these two pieces of information . Use the function to make three
# dictionaries representing different albums . Print each return value to 
# show that the dictionaries are storing the album information correctly . 
# Add an optional parameter to make_album() that allows you to store the 
# number of tracks on an album . If the calling line includes a value for 
# the number of tracks, add that value to the album’s dictionary . Make at 
# least one new function call that includes the number of tracks on an album.


def make_album(title, artist, tracks = 0):
    if tracks == 0:
        info = {"title" : title, "artist" : artist}
        return info
    elif tracks > 0:
        info = {"title" : title, "artist" : artist, "tracks" : tracks}
        return info
#libandeal = make_album("Real Good Deal", "Jim Liban")
#rhapsodylegend = make_album("Legendary Tales", "Rhapsody")
#shellistsessions = make_album("Chicago Sessions", "Ronnie Shellist", 12)
#print(libandeal)
#print(rhapsodylegend)
#print(shellistsessions)
print("Give me the album you want to print! Type 'q' at any point to exit"
    " and print.")
while True:
    title = input("What's the name of the album? ")
    artist = input("Who is the artist that recorded it? ")
    more = input("Do you want to include the number of tracks? (y/n) ")
    if more == "y":
        tracks = int(input("How many tracks are on the album? "))
    again = input("Do you need to retype anything? (y/n) ")
    if again == "n":
        break

album = make_album(title, artist, tracks)
print(album)
#8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
# loop that allows users to enter an album’s artist and title . Once you 
# have that information, call make_album() with the user’s input and print 
# the dictionary that’s created . Be sure to include a quit value in the 
# while loop .