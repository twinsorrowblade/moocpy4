# Write your solution here
# a_lowercase = ("")

# while a_lowercase != "visual studio code":
#     a = input("Editor: ")
#     a_lowercase = a.lower()

#     if a_lowercase != "visual studio code":
#         print("awful")
#     if a_lowercase == "visual studio code":
#         print("an excellent choice!")
#         break

while True:
    editor = input("Editor: ")
    editor_lowercase = editor.lower()
 
    if editor_lowercase == "visual studio code":
        print("an excellent choice!")
        break
    elif editor_lowercase in ["emacs", "vim", "atom"]:
        print("not good")
    else:
        print("awful")