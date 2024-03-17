from queue import Queue
import sys

#initialize queue for storing patient names
patients = Queue()
current_patient = None

while True:
    print ("Destop Manager - Patient Registration and Appointment system\n")
    print("""
        1. Press 1 to Rgister the patient
        2. press 2 to Remove the Patient
        3. Press 3 to Display the Patient
        4. Press 4 to Exit1
       """)
    userinput = input(">>>")
    print()

    if userinput == "1" :
        patient_name = input("Enter patient name:")
        patients.put(patient_name)
        current_patient = patient_name
        print(f"patient {patient_name} successfully Registered\n")

    elif userinput == "2":
        patients.get()
        print (f"patient {current_patient} removed after meeting the doctor.\n")
    
    elif userinput == "3":
        print("current patient Queue")
        for i in patients.queue:
            print (i)

    elif userinput == "4":
        print("Exited")
        sys.exit()

    else:
        print("Invalid input. Follow the Instruction well.\n\n")

