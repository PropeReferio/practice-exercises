def checkpal(pal):
  revpal = ""
  l = len(pal)
  while l > 0:
    revpal += pal[l-1]
    l -= 1
  
  if pal == revpal:
    print("Yes, that's a palindrome!")
  else:
    print("Nope! That's not a palindrome!")
    
checkpal(input("Give me a palindrome!"))