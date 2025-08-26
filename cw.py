# 1) კომენტარის სახით ახსენით რა განსხვავებაა  while loop-სა და for loop-ს შორის.

# while loop და for loop განსხვავდება იმით, რომ:
# while loop-ში ციკლი გრძელდება მანამ, სანამ მოცემული პირობა ჭეშმარიტია
# for loop კი ძირითადად გამოიყენება მაშინ, როცა ზუსტად ვიცით რამდენჯერ უნდა იმუშაოს ციკლმა.

# 2) for loop-ის დახმარებით გამოიტანეთ ყველა ლუწი რიცხვი 10-დან 50-მდე.

for num in range(10, 50, 2):
        print(num)

# 3) while loop-ის დახმარებით გამოიტანეთ ყველა კენტი რიცხვი 0-დან 20-მდე.

num = 0
while num <= 20:         
    if num % 2 != 0:
        print(num)
    num += 1

# 4) მომხმარებელს შემოატანინეთ რაიმე სიტყვა და ამ სიტყვას for loop-ით გადაუარეთ, გამოიტანეთ ამ სიტყვის ყველა ასო.

word = input("შეიყვანე სიტყვა: ")

for letter in word:
    print(letter)


# 5) მომხმარებელს შემოატანინეთ თავისი ასაკი, თუ მისი ასაკი ნაკლებია 18-ზე გამოიტანეთ "you are a child", თუ ტოლია 18-ის გამოიტანეთ "you just became an adult", ხოლო დანარჩენ შემთხვევებში გამოიტანეთ "you are an adult". გამოიყენეთ if/else.

age = int(input("შეიყვანე შენი ასაკი: "))

if age < 18:
    print("you are a child")
elif age == 18:
    print("you just became an adult")
else:
    print("you are an adult")