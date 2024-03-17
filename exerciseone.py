from queue import LifoQueue
import sys
patient_list = LifoQueue()
current_list = None
while True:
    print("Welcome to CST Infirmary Appointment and Registration System!")
    print("""Desk Manager-select the option below:
          1. Register patient
          2. Remove patient from the queue
          3. Display queue
          4. Exit""" )
    opt = int(input("Select an option from the above (1/2/3/4):"))

    if opt == 1:
        name = input("Enter the name of the patient:")
        patient_list.put(name)
        current_list = name
        print(f"{name} successfully Registered. Thank You! ")

    elif opt == 2:
        patient_list.get()
        print(f"{current_list} Successfully Removed from the queue after meeting with the doctor!")

    elif opt == 3:
        for i in patient_list.queue:
         print(i)


    elif opt == 4:
        print("Thank you for the Registration!")
        sys.exit()

    else:
        print("invalid syntax!")