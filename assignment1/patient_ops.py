import assignment1.patient_record as pr
import os.path as path


patient_records = pr.PatientRecords()

count = 0

if not path.exists("output.txt"):
    output = open("output.txt", "w+")
else:
    output = open("output.txt", "w+")

ps5file = open("input.txt", 'r')
for i in ps5file:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')
    name, age = (i.split(","))
    patient_records.register_patient(name, age)
    count += 1
    print(patient_records.patients)

output.write("---- initial queue ---------------\n"
             + "No of patients added: " + str(count)
             + "\n Refreshed queue:")


# for i in patient_records.get_patients()

print(patient_records.patients)
patient_records.register_patient("Raj1", 68)
patient_records.register_patient("Raj2", 26)
patient_records.register_patient("Raj3", 96)
patient_records.register_patient("Raj4", 75)
patient_records.register_patient("Raj5", 88)
patient_records.register_patient("Raj6", 56)
patient_records.register_patient("Raj7", 45)
patient_records.register_patient("Raj8", 70)
patient_records.register_patient("Raj9", 18)
patient_records.register_patient("Raj10", 90)
print(patient_records.patients)
patient_records.next_patient()
patient_records.dequeue_patient(patient_records.next_patient().pat_id)
print(patient_records.patients)
patient_records.heap_sort(patient_records.patients)
print(patient_records.patients)
output.close()
