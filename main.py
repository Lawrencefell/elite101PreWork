## opening
loop = True
print("welcome to the prework bot")
name = input("what is your name: ")
age = input("how old are you: ")

## interaction 
while loop:
  print("how may I help you?")
  responce = input("""
1 = text sample 1
2 = text sample 2
3 = text sample 3
4 = exit
 """)
  if responce == "1":
    print("text")
  if responce == "2":
    print("text")
  if responce == "3":
    print("text")
  if responce == "4":
    loop = False
print("have a nice day.")
print("goodbye")
quit()