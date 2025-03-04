import os

if __name__ == '__main__':
    file_location = ".\\file_handling\demofile.txt"
    file = open(file_location, "r")
    # print(file.read())

    # print(file.read(10)) # read the first 10 caracter

    # print(file.readline()) # read the first line, if you write this line it will print the second line

    # for i in file: 
    #     print(i)

    # file.close()

    file_location_2 = ".\\file_handling\demofile2.txt"
    # file = open(file_location2, "a")
    # file.write("Now the file is more content!")
    # file.close()

    # file = open(file_location2, "r")
    # print(file.read())

    # file = open(file_location2, "w")
    # file.write("Woops! I have deleted the content!")
    # file.close()

    # file = open(file_location2, "r")
    # print(file.read())

    # "x" - Create - will create a file, returns an error if the file exists

    # os.remove(file_location_2)

    if os.path.exists(file_location_2):
        os.remove("file_location_2")
    else:
        print("The file does not exist")


    # remove a folder
    # os.rmdir("myfolder")