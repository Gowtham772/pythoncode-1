#Problem Statement:
#Write a Python program to create a list of software application details. The details of application include name, author, version, publishing year , price

#Perform the following with respect to the list of application created.

#a) Display all the details of application by a given author.

#b) Sort the details of application in the increasing order of price.

#c) Display the details of applications published by a given publisher in a given year.

#d) Sort the list of applications in the increasing order of two fields , author and publishing year of the books.
#Solution:
#This program is used to create a list of application,
# to display all the details of application by a given author,
# to sort the details of application in the increasing order of price,
# to display the details of applications published by a given publisher in a given year,
# to sort the list of applications in the increasing order of two fields , author and publishing year of the books.
print("Enter the below details to create the database...")
print("Enter the details must be separated by spaces....")
print("The program will ask you for Author name/anything, just give the input of the data in the same line and each of the input(name/other) data must be separated by space...")
print("For example:\n If it shown as , Enter the Author names : enter the input like:: ""Shakespeare Henry Faulker JaneAusten"", if you entered all the data that you had means just click Enter to move to next process ")
print("Confirm that your enter the data in an order and enter the same number of data in all blocks...")
i = 0
j = 1
k = 1
input1_string = input('Enter the Author names separated by space: ')
input2_string = input('Enter the Books name separated by space :')
input3_string = input('Enter the Books version separated by space:')
input4_string = input('Enter the Pulished year of the books separated by space: ')
input5_string = input('Enter the Costs of the Book separated by space:')
print("\n")
Author_name = input1_string.split()
Book_name = input2_string.split()
Book_version = input3_string.split()
Published_year = input4_string.split()
a = input4_string.split()
Book_cost = input5_string.split()
b = input5_string.split()

print(
    "Enter 1 to Display all the details of application by a given author\n"
    "Enter 2 to Sort the details of application in the increasing order of price\n"
    "Enter 3 to Display the details of applications published by a given publisher in a given year\n"
    "Enter 4 to Sort the list of applications in the increasing order of two fields , author and publishing year of the books\n"
    "Enter 5 to Exit")
while k == 1:
    choice = int(input('Enter the choice:'))
    Book_cost = input5_string.split()
    if choice == 1:
        j = 0
        f = input('Enter the author name:')
        for i in range(0, len(Author_name)):
            if f == Author_name[i]:
                print('Author_name:' + Author_name[i] + ',Book_name:' + Book_name[
                    i] + ',Book_version:' + Book_version[i] + ',Published_year:' +
                      Published_year[i] + ',Book_cost:' + Book_cost[i])
                j = 0
            elif j == 1 and i == len(Author_name) - 1:
                print("No Books available...")

    if choice == 2:
        for i in range(0, len(Book_cost)):
            Book_cost[i] = int(Book_cost[i])
            b[i] = int(b[i])
        for i in range(0, len(Book_cost)):
            for j in range(i + 1, len(Book_cost)):
                if b[i] > b[j]:
                    temp = b[i]
                    b[i] = b[j]
                    b[j] = temp
        for i in range(0, len(Book_cost)):
            for j in range(0, len(Book_cost)):
                if b[i] == Book_cost[j]:
                    print('Author_name:' + Author_name[j] + ',Book_name:' + Book_name[
                        j] + ',Book_version:' + Book_version[j] + ',Published_year:' +
                          Published_year[j]+'\nBook_cost:' )
                    print( Book_cost[j])

    if choice == 3:
        m = 1
        f = input("Enter the Author name:")
        y = input("Enter the Published year of the book:")
        for i in range(0, len(Author_name)):
            if f == Author_name[i]:
                if y == Published_year[i]:
                    print('Author_name:' + Author_name[i] + ',Book_name:' + Book_name[
                        i] + ',Book_version:' + Book_version[i] + ',Published_year:' +
                          Published_year[i] + ',Book_cost:' + Book_cost[i])
                    m = 0
            elif m == 1 and i == len(Author_name)-1:
                print("No Books available...")

    if choice == 4:
        m = 1
        f = input("Enter the Author Name:")
        for i in range(0, len(Published_year)):
            for j in range(i + 1, len(Published_year)):
                if a[i] > a[j]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
        for i in range(0, len(Published_year)):
            for j in range(0, len(Published_year)):
                if a[i] == Published_year[j]:
                    if f == Author_name[j]:
                        print('Author_name:' + Author_name[j] + ',Book_name:' + Book_name[
                            j] + ',Book_version:' + Book_version[j] + ',Published_year:' +
                              Published_year[j] + ',Book_cost:' + Book_cost[j])
                        m = 0
                elif m == 1 and i == len(Published_year)-1:
                    print("No Books available...")
    if choice == 5:
        exit()

