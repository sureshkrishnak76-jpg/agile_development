numbers=[10,20,30,40]
print("Sum=",sum(numbers))
print("Maximun=",max(numbers))
print("Average=",sum(numbers)/len(numbers))

print("\n")

temperature=30
if temperature>35:
    print("Wear light cloths.")
elif temperature>20:
    print("weather is pleasant.")
else:
    print("Wear a sweater.")

print("\n")

fever="yes"
cough="yes"
if fever=="yes" and cough=="yes":
    print("Possible Flu")
elif fever=="yes":
    print("Possible Viral Fever 123456789")
else:
    print("No major symptoms detected.")

print("\n")

msgs=["hello","how are you","bye"]
for msg in msgs:
    if msg=="hello": print("Bot: Hello!")
    elif msg=="how are you": print("Bot: I am fine.")
    elif msg=="bye": print("Bot: Goodbye!")

print("\n")

numbers=[3,8,10,15,22]
target=15
print("Found" if target in numbers else "Not Found")

print("\n")

legs=4
sound="bark"
if legs==4 and sound=="bark" : print("Dog")
elif legs==4 and sound=="meow": print("Cat")
elif legs==2: print("Bird")
else: print("Unknown")


