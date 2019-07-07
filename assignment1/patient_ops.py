import assignment1.patient_record as pr
import os.path as path


patient_records = pr.PatientRecords()

count = 0

if not path.exists("output.txt"):
    output = open("output.txt", "w+")
else:
    output = open("output.txt", "w+")

inputps5afile = open("inputPS5a.txt", 'r')
for i in inputps5afile:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')
    name, age = (i.split(","))
    patient_records.register_patient(name, age)
    count += 1
    print(patient_records.patients)

output.write("---- initial queue ---------------\n"
             + "No of patients added: " + str(count)
             + "\nRefreshed queue:\n")
patient_records.heap_sort(patient_records.patients)

for i in range(len(patient_records.patients)-1, -1, -1):
    temp = patient_records.find_patient(patient_records.patients[i])
    output.write(temp.pat_id + ", " + temp.name + "\n")

output.write("----------------------------------------------")
# for i in patient_records.get_patients()
patient_records.build_heap(patient_records.patients)

inputPS5bfile = open("inputPS5b.txt", "r")
for i in inputPS5bfile:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')

    if i[0:3] == "new":
        key, temp = i.split(":")
        name, age = (i.split(","))
        patient_records.register_patient(name, age)
        # count += 1
        output.write("---- new patient entered---------------\n" + "Patient details: "
                + name + ", " + str(age) + ", " + str(patient_records.num) + str(age) + "\n" + "Refreshed queue: \n")
        patient_records.heap_sort(patient_records.patients)
        for j in range(len(patient_records.patients)-1, -1, -1):
            temp = patient_records.find_patient(patient_records.patients[j])
            output.write(temp.pat_id + ", " + temp.name + "\n")
        output.write("----------------------------------------------")
        patient_records.heap_sort(patient_records.patients)
        print(patient_records.patients)
    elif i[0:3] == "nex":
        output.write("---- next patient ---------------")
        temp = patient_records.next_patient()
        output.write("Next patient for consultation is: " + temp.pat_id + ", " + temp.name)
        output.write("----------------------------------------------")
        patient_records.dequeue_patient(temp.pat_id)




# patient_records.heap_sort(patient_records.patients)
# patient_records.register_patient("Raj1", 68)
# temp = self.find_patient(pat_id)

# print("---- new patient entered---------------\n")
# print("Patient details: " + temp.name+", " + str(temp.age) + ", " + temp.pat_id+"\n")
# print("Refreshed queue: ")
#
#
# print(patient_records.patients)
# patient_records.register_patient("Raj1", 68)
# patient_records.register_patient("Raj2", 26)
# patient_records.register_patient("Raj3", 96)
# patient_records.register_patient("Raj4", 75)
# patient_records.register_patient("Raj5", 88)
# patient_records.register_patient("Raj6", 56)
# patient_records.register_patient("Raj7", 45)
# patient_records.register_patient("Raj8", 70)
# patient_records.register_patient("Raj9", 18)
# patient_records.register_patient("Raj10", 90)
# print(patient_records.patients)
# patient_records.next_patient()
# patient_records.dequeue_patient(patient_records.next_patient().pat_id)
# print(patient_records.patients)
# patient_records.heap_sort(patient_records.patients)
# print(patient_records.patients)
output.close()
