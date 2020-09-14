import csv
def write_into(info):
    with open("student_info.csv", "a", newline="") as csv_files:
        writer = csv.writer(csv_files)
        if csv_files.tell() ==0:
            writer.writerow(["Name","AGE","contact number","Email ID","Admission no."])
        writer.writerow(info)
def call():
    if __name__ == '__main__':
        condition = True
        student_no = 1

        while (condition):
            student_info = input(
                "Enter student information for student[{}] \nin the following order with a comma in between(Name,Age,Contact number,Email ID and admission no.):"
                " ".format(
                    student_no))

            student_info_list = student_info.split(",")
            print("\nThe entered information is-\nName: {}\nAge: {}\nContact number: {}\nEmail-ID: {}\nAdmission no.: {}"
                  .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4]))

            confirmation = input("Is the above entered information correct(yes/no): ")
            if confirmation == "yes":
                condition = True
                write_into(student_info_list)
                condition_check = input("Enter yes or no if you want to enter another student information: ")

                if condition_check == "yes":
                    condition = True
                    student_no = student_no + 1
                elif condition_check == "no":
                    condition = False
            elif confirmation == "no":
                print("\nPlease re-enter the value: ")
#available users and passwords
username_ = ["user1","user2","user3","user4"]
passwords = ["pass123","pass234","pass345","pass456"]
Condition = True
while(Condition):
    print("*******WELCOME TO THE LOGIN PAGE*******")
    print("Please login to procced further- ")
    username = input("USERNAME: ")
    if username in username_:
        Condition = True
        print("Please enter the password for "+username+":")

        password = input("PASSWORD: ")
        if password in passwords:
            Condition = True
            print("Access granted!")
            call()
        elif password not in passwords:
            print("Wrong combination")
            print("Please re-login")
    elif username not in username_:
        print("   Username does not exist\n  Try again")
