# 1) შედარების ოპერაციებზე გააკეთეთ 10-10 მაგალითი თოთოეულ მაგალითს კომენტარის სახით მიუწერეთ რას დააბრუნებს ჩვენი კოდი 
# მეტობა:
print(56 > 23) # True
print(68 > 12) # True
print(23 > 1) # True
print(65 > 12) # True
print(12 > 6) # True
print(23 > 54) # False
print(12 > 147) # False
print(7 > 43) # False
print(543 > 789) # False
print(134 > 456) # False
# ნაკლებობა:
print(534 < 623) # True
print(123 < 688) # True
print(678 < 999) # True
print(145 < 456) # True
print(567 < 987) # True
print(244 < 114) # False
print(6112 < 311) # False
print (1235 < 1155) # False
print(244 < 43) # False
print(2 < 1) # False
# 2) კომენტარის სახით ახსენით რა არის boolean'ი 
# boolean არის ერთ-ერთი მონცაცემთა ტიპი რომელიც არის მხოლოდ True და False
#3) რას ნიშნავს კომპიუტერის ენაზე 1 და 0 
# 1-ები და 0-ები ერთად არის binary code, რომელიც არის ენა, რითიც იგებს კომპიუტერი კოდებს.
# 4) კომენტარის სახით ახსენით and oპერატორი
# and ოპერატორი გამოიყენება True და False-თან. and როცა წერია, რამდენი Trueც არ უნდა ეწეროს, 1 False-იც რო იყოს, False'ს გამოიტანს.
# 5) კომენტარის სახით ახსენით or ოპერატორი 
# or ოპერატორი გამოიყენება True და False-თან. or როცა წერია, რამდენი Falseიც არ უნდა ეწეროს, 1 True-ც რო იყოს, Trues'ს გამოიტანს.
# 6) and oპერატორის გამოყენებით დაწერეთ 10 მაგალითი თითოეულს გვერდით კომენტარის სახით დაუწერეთ თუ რას გამოიტანს იქამდე სანამ კონსოლში გაუშვებთ
print(True and True) # True 
print(True and False) # False 
print(False and True) # False 
print(False and False) # False 
print(5 > 3 and 2 < 4) # True 
print(10 == 10 and 5 != 5)  # False 
print(3 and 7) # 7 
print(0 and 5) # 0 
print([] and "hello") # [] 
print("text" and 123) # 123 
# 7) or oპერატორის გამოყენებით დაწერეთ 10 მაგალითი თითოეულს გვერდით კომენტარის სახით მიუწერეთ თუ რას გამოიტანს ეს კოდი იქამდე სანამ კონსოლში გამოიძახებთ 
print(True or False) # True 
print(False or True) # True 
print(False or False) # False 
print(0 or 5) # 5 
print("" or "hello") # "hello" 
print([] or [1, 2]) # [1, 2] 
print("Python" or "Java") # "Python" 
print(None or "default") #"default" 
print(False or 0) # 0 
print(0 or False) # False
# 8) შედარების და ლოგიკური ოპერაციები გააერთიანეთ და მათზეც გააკეთეთ 5 მაგალითი
print(5 > 3 and 2 < 4) # True 
print(10 == 10 or 7 < 5) # True 
print(8 != 8 and 4 > 1) # False 
print(not (3 >= 3)) # False 
print((2 < 5 or 9 < 4) and 1) # 1
# 9) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ რიცხვს შემდეგ ამ ცვლადის მნიშვნელობა გაზარდეთ 10'ით პრინტით გამოიძახეთ ეს ცვლადი და მოახდინეთ მასზე შედარების ოპერაცია ისე რომ გამოიტანოს True
num = 25
num = num + 10
print(num) # 35
print(num > 30)  # True 
# 10) შექმენით ცვლადი temperature სადაც შეინახავთ 30 გრადუსს თუ 30 გრადუსზე მეტი იქნება რაიმე რიცხვი გამოიტანეთ  True 
temperature = 30
print(temperature > 25) # True