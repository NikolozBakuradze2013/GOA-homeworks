# 1) კომენტარეის სახით ახსენით რას ნიშნავს immutable და mutable.

# immutable არის შეუცვლელი, და mutable შესაძლებელი რომ შეცვალო.
# მაგალითად, string-ები immutable-ები არის, და list-ები mutable-ები

# 2) შექმენით სია 10 ელემენტით და შემდგომ ჩაანაცვლეთ მეხუთე ელემენტი "goa"-თი.

elements10 = ["hi", "my", "name", "is", "niko", "nice" "to" "meet" "you" "bye"]
elements10[4] = "goa"

# 3) შექმენით ცვლადი სადაც მომხმარებელი შეინახავს რიცხვს, შემდეგ მომხმაერებელს შემოატანინეთ რიცხვი, სანამ მომხმარებელი არ გამოიცნობს თქვენს შენახულ რიცხვს გამოიტანეთ: "არასწორია თავიდან ცადე" და თავიდან შემოატანინეთ input, თუ გამოიცნობს გამოიტანეთ: "შენ გამოიცანი რიცხვი".

secret_number = 7

guess = int(input("Think of a number: "))

while guess != secret_number:
    print("Wrong, try again")
    guess = int(input("Think of a number: "))

print("You guessed the number!")


# 4) გაამარტივეთ და კომენტარის სახით დაწერეთ რას გამოიტანს ქვემოთ მოეცემული კოდი:
# print(True and False or False or True and (False and False) or (True and True) or (False or True) or False or True and False) ეს კოდი არ გაუშვათ.

# გავხსნათ ნელ-ნელა:

# True and False → False
# True and (False and False) → True and False → False
# (True and True) → True
# (False or True) → True
# True and False → False

# კოდი გადადის ასეთ ფორმაში:
# False or False or False or True or True or False or True

# "or"-ში თუ ერთი მაინც Trueა, შედეგი იქნება True.
# აქ გვაქვს რამდენიმე True, ამიტომ საბოლოო შედეგი იქნება True.

# პასუხი: True
