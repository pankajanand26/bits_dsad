import assignment1.patient_record as pr
import os.path as path


patient_records = pr.PatientRecords()

count = 0

if not path.exists("outputPS5.txt"):
    output = open("outputPS5.txt", "w+")
else:
    output = open("outputPS5.txt", "w+")

inputps5afile = open("inputPS5a.txt", 'r')
for i in inputps5afile:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')
    name, age = (i.split(","))
    patient_records.register_patient(name, age)
    count += 1
    # print(patient_records.patients)

output.write("---- initial queue ---------------\n"
             + "No of patients added: " + str(count)
             + "\nRefreshed queue:\n")
patient_records.heap_sort(patient_records.patients)

for i in range(len(patient_records.patients)-1, -1, -1):
    temp = patient_records.find_patient(patient_records.patients[i])
    output.write(temp.pat_id + ", " + temp.name + "\n")

output.write("----------------------------------------------")
# for i in patient_records.get_patients()
# print(patient_records.patients)
# print("hi hello")
patient_records.build_heap(patient_records.patients)
# print(patient_records.patients)
inputPS5bfile = open("inputPS5b.txt", "r")
for i in inputPS5bfile:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')

    if i[0:3] == "new":
        key, temp = i.split(":")
        name, age = (temp.split(","))
        # print(name,age)
        patient_records.register_patient(name, age)
        output.write("\n---- new patient entered---------------\n" + "Patient details: "
                    + name + ", " + str(age) + ", " + str(patient_records.num)
                    + str(age) + "\n" + "Refreshed queue: \n")
        patient_records.heap_sort(patient_records.patients)
        # print(patient_records.patients)
        # patient_records.get_patient_list()
        # patient_records.get_head_patient_list()
        for j in range(len(patient_records.patients)-1, -1, -1):
            # print(patient_records.head.pat_id)
            temp = patient_records.find_patient(patient_records.patients[j])
            output.write(temp.pat_id + ", " + temp.name + "\n")
        output.write("----------------------------------------------")
        # print(patient_records.patients)
        patient_records.build_heap(patient_records.patients)
        # print(patient_records.patients)
    elif i[0:3] == "nex":
        output.write("\n---- next patient ---------------")
        temp = patient_records.next_patient()
        if temp:
            output.write("\nNext patient for consultation is: " + temp.pat_id + ", " + temp.name)
            output.write("\n----------------------------------------------")
            delete_flag = patient_records.dequeue_patient(temp.pat_id)
        else:
            output.write("\nNo patient in consultation queue.")
            output.write("\n----------------------------------------------")

output.close()
