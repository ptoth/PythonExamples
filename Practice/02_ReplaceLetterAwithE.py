myText = "This text is a sample"
print("Our sample text is: "+myText)
print(myText.replace("a","e"))

# reminder: replacing does not overwrite the original variable
print(myText)

# but this will:
myText = myText.replace("a","e")
print(myText)