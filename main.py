



from textblob import TextBlob
 
user = input("Type something:  ")  # Wrong spelling

print("original text: "+str(user))
 
b = TextBlob(user)
 
# prints corrected spelling
print("corrected text: "+str(b.correct()))


