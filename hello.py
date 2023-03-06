# greetings based on users' names
name = input("What is your name? ").title().strip()

greeting = {
    'Giorgi': "Hello, Giorgi, it's nice to see you.",
    'Nino': "Hello, Nino, how are you?",
    'Levani': "Good day Levan, how is your day going?",
    'Tamari': "Hello Tamar, hope you are having a wonderful day"
}

if name in greeting:
    print(greeting[name])
else:
    print("Hello,", name)