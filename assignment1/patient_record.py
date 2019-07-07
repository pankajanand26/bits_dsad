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

    # def __init__(self):
    #     print("PR ")

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
        while temp.pat_id != pat_id:
            temp = temp.right
        return temp

    def register_patient(self, name, age):
        print("register_patient")
        if self.head is None:
            self.head = PatientClass(name, age, self.num+1)
            self.tail = self.head
            self.num += 1
            # self.patients.append(self.head.pat_id)
        else:
            self.head.right = PatientClass(name, age, self.num + 1)
            self.head.right.left = self.head
            self.head = self.head.right
            # self.patients.append(self.head.pat_i
            # d)
            self.num += 1
        self.enqueue_patient(self.head.pat_id)

    def enqueue_patient(self, pat_id):
        print("Insert "+pat_id+" into max heap.")
        self.patients.append(pat_id)
        self.upheap(self.patients)

    def next_patient(self):
        print("Dequeue Patient as per call.")
        temp = self.find_patient(self.patients[0].pat_id)
        print('''---- next patient - --------------
            Next patient for consultation is: '''+temp.pat_id+", " + temp.name+
            '''----------------------------------------------''')

    def get_age(self, a):
        return int(a[-2:])

    def build_heap(self, a, size=-1):
        print("build_heap")
        if size == -1:
            heap_size = len(a)
        else:
            heap_size=size
        # print("Length of a is " + str(heap_size))
        for i in range(heap_size//2, 0, -1):
            self.heapify(a, i, heap_size)
            # print(a)
        return a

    def heapify(self, a, i, size=-1):
        print("heapify")
        max = i-1
        if size == -1:
            heap_size = len(a)
        else:
            heap_size = size
        l = 2*i-1
        r = 2*i
        l = 2*i + 1
        r = 2*i + 2
        # if l < heap_size and a[max].age < a[l].age:
        #    max = l
        if l < heap_size and self.get_age(a[max]) < self.get_age(a[l]):
            max = l

        # if r < heap_size and a[max].age < a[r].age:
        #     max = r
        if r < heap_size and self.get_age(a[max]) < self.get_age(a[r]):
            max = r
        if max != i-1:
            a[i-1], a[max] = a[max], a[i-1]
            self.heapify(a, max+1, heap_size)

    def upheap(self, a):
        heap_size = len(a)
        print("upheap")
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

    def get_top(self, a):
        heap_size = len(a)
        print("get_top")
        # temp = None
        # a[0], a[heap_size-1] = a[heap_size-1], a[0]
        temp = a[heap_size-1]
        # del a[heap_size-1]
        # self.heapify(a, 1, heap_size - 1)
        # build_heap(a, heap_size-1)
        return temp

    def heap_sort(self, a):
        print("heap_sort")
        heap_size = len(a)
        self.build_heap(a, heap_size)
        while heap_size > 1:
            a[0], a[heap_size-1] = a[heap_size-1], a[0]
            self.heapify(a, 1, heap_size-1)
            heap_size -= 1
            # print(a)

