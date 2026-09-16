sentence = input("Enter your sentence:")
chrch = input("Enter a single character:")
i = 0
count = 0
while i < len(sentence):
    if sentence[i] == chrch:
        count = count+1
    
    i+= 1
print(count)    