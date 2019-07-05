import assignment1.patient_record as pr


patient_records = pr.PatientRecords()

ps5file = open("input.txt", 'r')
for i in ps5file:
    removal_list = [' ', '\t', '\n']
    for s in removal_list:
        i = i.replace(s, '')
    name, age = (i.split(","))
    patient_records.register_patient(name, age)

print(patient_records.patients)
patient_records.build_heap(patient_records.patients)
print(patient_records.patients)

patient_records.register_patient("Raj", 68)
# patient_records.get_patient_list()
print(patient_records.patients)
patient_records.build_heap(patient_records.patients)
print(patient_records.patients)
# patient_records.get_patient_list()
# patient_records.heap_sort(patient_records.patients)
# print(patient_records.patients)
patient_records.get_top(patient_records.patients)
print(patient_records.patients)
print(patient_records.get_head_patient_list())
# pr.PatientRecord("",0,0).build_heap(p)
# for i in p:
#     print(i.pat_id)
#
# p.append(pr.PatientRecord("John",65,pr.PatientRecord.num+1))
# print(p[3].age)
# pr.PatientRecord("",0,0).upheap(p)
# pr.PatientRecord("",0,0).build_heap(p)
# for i in p:
#     print(i.pat_id)
#
# pr.PatientRecord("",0,0).heap_sort(p)
# for i in p:
#     print(i.pat_id)
