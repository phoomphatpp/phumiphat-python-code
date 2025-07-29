"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to: เปิดโอกาสให้ผู้ใช้สามารถ

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    person = ("Elliot", 20, "Bangkok", "Thailand")  # name, age, city, country
    hobbies = []
    while True:
    # Create initial person tuple
        # print("\n1. Display all information")
        # print("2.Add new hobbies")
        # print("3.Remove hobbies")
        # print("4.Update age")
        choice = input("\n1. Display all information " \
        "\n2.Add new hobbies" \
        " \n3.Remove hobbies" \
        " \n4.Update age" \
        " \n5.exit " \
        "\nSelect Menu :")
        if(choice == "1"):
        # display all info
            print("")
            print("Show all Information")
            print("Name :",person[0])
            print("Age :",person[1])
            print("City :",person[2])
            print("Country :",person[3])
            print(f"Hobbies: {hobbies}")

        elif(choice =="2"):
            # append hobbie
            print("Add Hobbies")
            hobby = input("enter hobby :")
            hobbies.append(hobby)
        elif(choice =="3"):
            # remove hobbie
            print("Delete Hobbies")
            if hobbies:
                hobbies.pop()
            else:
                print("Hobbies is empty")
        elif(choice == "4"):
            # แปลงโดยใช้ list() จาก tuple
            person_list = list(person)
            new_age = input("How old Are you? :")
            person_list[1] = int(new_age)
            person = tuple(person_list)
        elif(choice =="5"):
            print("Exit")
            break
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()

