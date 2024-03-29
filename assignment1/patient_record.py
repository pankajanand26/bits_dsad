class PatientClass:
    # num = 1000

    def __init__(self,name, age, pid):
        self.pat_id = str(pid)+str(age)
        self.name = name
        self.age = int(age)
        self.left = None
        self.right = None


class PatientRecords:
    num = 1000
    patients = []
    head = None
    tail = None

    def get_patients(self):
        for i in self.patients:
            print(i)

    def get_patient_list(self):
        temp = self.tail
        while temp is not None:
            print(temp.pat_id,": "+temp.name)
            temp = temp.right

    def get_head_patient_list(self):
        temp = self.head
        while temp is not None:
            print(temp.pat_id,": "+temp.name)
            temp = temp.left

    def find_patient(self, pat_id):
        temp = self.tail
        while temp is not None and temp.pat_id != pat_id:
            temp = temp.right
        return temp

    def delete_patient(self, pat_id):
        temp = self.tail
        previous = None
        if temp is None:
            return

        while temp is not None and temp.pat_id != pat_id:
            previous = temp
            # print(temp.name, temp.pat_id)
            temp = temp.right

        if previous is None:
            if temp.right is None:
                self.tail = None
                del temp
            else:
                self.tail = temp.right
                self.tail.left = None
                del temp
        elif temp.right is None:
            previous.right = None
            self.head = temp.left
            del temp
        else:
            previous.right = temp.right
            temp.right.left = previous
            del temp
        # print(self.get_patient_list())

    def register_patient(self, name, age):
        print("register_patient")
        if self.head is None:
            self.head = PatientClass(name, age, self.num+1)
            self.tail = self.head
            self.num += 1
        else:
            print(self.head.pat_id)
            self.head.right = PatientClass(name, age, self.num + 1)
            self.head.right.left = self.head
            self.head = self.head.right
            print(self.head.pat_id, self.tail.pat_id)
            self.num += 1
        self.enqueue_patient(self.head.pat_id)

    def enqueue_patient(self, pat_id):
        # print("Insert "+pat_id+" into max heap.")
        self.patients.append(pat_id)
        self.upheap(self.patients)
        # temp = self.find_patient(pat_id)
        # message = "---- new patient entered---------------\n" + "Patient details: "
        # + temp.name+", " + str(temp.age) + ", " + temp.pat_id+"\n" + "Refreshed queue: "
        # return message


    def next_patient(self):
        print("Next Patient as per queue.")
        if len(self.patients) !=0:
            temp = self.find_patient(self.patients[0])
            return temp
        else:
            return False

    def dequeue_patient(self, pat_id):
        print("Dequeue "+pat_id+" from the queue")
        heap_size = len(self.patients)
        if heap_size != 0:
            index = -1
            for i in range(0, heap_size):
                if self.patients[i] == pat_id:
                    index = i
            if index == -1:
                print("Patient not in the list.")
                return
            self.patients[index], self.patients[heap_size-1] = self.patients[heap_size-1], self.patients[index]
            temp = self.patients[heap_size-1]
            self.heapify(self.patients, index, heap_size - 1)
            self.delete_patient(temp)
            del self.patients[-1]
            return True
        else:
            return False

    def get_age(self, a):
        return int(a[-2:])

    def build_heap(self, a, size=-1):
        # print("build_heap")
        if size == -1:
            heap_size = len(a)
        else:
            heap_size = size
        # print("Length of a is " + str(heap_size))
        for i in range(heap_size//2, -1, -1):
            self.heapify(a, i, heap_size)
            # print(a)
        # return a

    def heapify(self, a, i, size=-1):
        # print("heapify")
        max_index = i
        if size == -1:
            # print("default: "+str(len(a)))
            heap_size = len(a)
        else:
            # print("size: "+str(size))
            heap_size = size
        # l = 2*i-1
        # r = 2*i
        l = 2*i + 1
        r = 2*i + 2
        # print(a)
        # print(str(max_index)+" "+str(l)+" "+str(r)+" "+str(heap_size))
        # print(str(a[max_index])+" "+str(a[l])+" "+str(a[r]))
        if l < heap_size and self.get_age(a[max_index]) < self.get_age(a[l]):
            max_index = l

        if r < heap_size and self.get_age(a[max_index]) < self.get_age(a[r]):
            max_index = r

        if max_index != i:
            a[i], a[max_index] = a[max_index], a[i]
            # print(a)
            self.heapify(a, max_index, heap_size)
        # print(a)

    def upheap(self, a):
        heap_size = len(a)
        # print("upheap")
        i = heap_size-1
        if i % 2 == 0:
            parent = (i-2)//2
        else:
            parent = (i-1)//2
        while i > 0:
            if self.get_age(a[i]) > self.get_age(a[parent]):
                a[parent], a[i] = a[i], a[parent]
                i = parent
                if parent % 2 == 0:
                    parent = (parent-2)//2
                else:
                    parent = (parent-1)//2
            else:
                return

    def heap_sort(self, a):
        # print("heap_sort")
        heap_size = len(a)
        self.build_heap(a, heap_size)
        while heap_size > 1:
            a[0], a[heap_size-1] = a[heap_size-1], a[0]
            self.heapify(a, 0, heap_size-1)
            heap_size -= 1
            # print(a)

