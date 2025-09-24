
# Ask user for their name removes whitespace from a string ans capitilize 
#name = input("What is your name? ").strip().title()


# split int first and last name

#first,last = name.split(" ")
# says hello to the user 
#print(f"hello {name}")
#overide the end /n and with "???"
#print(f"hello {first}", end="???")



def main():
    name = input("Whats your name? ")
    name = hello(name)
    print(name)

def hello(to="default"):
    return(F"Hello {to}")


main()
     



