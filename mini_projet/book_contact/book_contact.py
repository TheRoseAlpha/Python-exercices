contact_dic = {}

name = input("Name: ")
number = input("Number: ")
contact_dic.update({name: number})


file_location = ".\\mini_projet\\book_contact\\contact_file.txt"
file_contact = open(file_location, "a")


for names, numbers in contact_dic.items():
    file_contact.write(f"{names} : {numbers}\n")


file_contact.close()
file_contact = open(file_location, "r")


for line in file_contact:
    print(line)


file_contact.close()