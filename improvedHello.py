# Ask user for their name
name = input("What's your name? ")

# Say hello to user 
#print("hello," , name) args seprated by one
#print("hello, " + name) concatenating
print("hello, " , end="")
print(name)

"""
 is a multiline comm ent
"""
print('Hello, "friend"') #printing qoutation marks
print("hello, \"friend\"") #another way of printing qoutaiotn marks

# frequently used way, esp for setting up longer strings
print(f"hello, {name}") #{name} is a format string, f - python understands it's a special form of format on a string