# დაწერე პრორამა რომელიც გკითხავს სახელს "What is your name?" და როცა უპასუხებ მოგესალმება შენი სახელის გამოყენებით. 

# მაგალითი: 
# What is your name? Oto
# Hello, Oto, nice to meet you!

# მოთხოვნები:
# დარწმუნდი რომ input, კონკატენაცია და output ცალ-ცალკე გაქვს.

# დამატებითი გამოწვევები:
# დაწერე იგივე პროგრამის მეორე ვერსია ოღონდ ამ შემთხვევაში საერთოდ აღარ გამოიყენო ცვლადები.
# შექმენი პროგრამის ისეთი ვერსია რომელიც სხვა და სხვა სახელის მქონე ადამიანებს განსხვავებული მისალმებით პასუხობს.

name = input("What is your name? ")
print(f"Hello, {name}, nice to meet you!")


# second version without variables
print("Hello, " + input("What is your name? " ) + ", nice to meet you!")

