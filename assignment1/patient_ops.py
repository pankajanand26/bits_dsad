import assignment1.patient_record as pr
import os.path as path


patient_records = pr.PatientRecords()

if not path.exists("output.txt"):
    output = open("output.txt","w+")
else:
    output = open("output.txt","a+")

ps5file = open("input.txt", 'r')
for i in ps5file:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')
    name, age = (i.split(","))
    patient_records.register_patient(name, age)
    print(patient_records.patients)

print(patient_records.patients)
patient_records.register_patient("Raj", 68)
print(patient_records.patients)
# patient_records.build_heap(patient_records.patients)
# print(patient_records.patients)
# patient_records.heap_sort(patient_records.patients)
# print(patient_records.patients)
# patient_records.get_top(patient_records.patients)
# print(patient_records.patients)
output.close()
