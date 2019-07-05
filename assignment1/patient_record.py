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
        # print(self.tail.name)
        temp = self.tail
        while temp is not None:
            print(temp.pat_id,": "+temp.name)
            temp = temp.right

    def get_head_patient_list(self):
            # print(self.tail.name)
            temp = self.head
            while temp is not None:
                print(temp.pat_id,": "+temp.name)
                temp = temp.left

    def register_patient(self, name, age):
        print("register_patient")
        if self.head is None:
            self.head = PatientClass(name, age, self.num+1)
            self.tail = self.head
            self.num += 1
            self.patients.append(self.head.pat_id)
        else:
            self.head.right = PatientClass(name, age, self.num + 1)
            self.head.left = self.head
            self.head = self.head.right
            self.patients.append(self.head.pat_id)
            self.num += 1

    def enqueue_patient(self, pat_id):
        print("Insert "+pat_id+" into max heap.")

    def dequeue_patient(self, pat_id):
        print("Dequeue Patient as per call.")

    def get_age(self, a):
        return int(a[-2:])

    def build_heap(self, a, size=-1):
        print("build_heap")
        if size == -1:
            heap_size=len(a)
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
        print(str(i))
        parent = i//2
        while i > 0:
            # print(str(a[i].age)+" " +str(a[parent].age))
            # print(str(type(a[i].age))+" "+str(type(a[parent].age)))
            # if a[i].age > a[parent-1].age:
            if self.get_age(a[i]) > self.get_age(a[parent-1]):
                a[parent-1], a[i] = a[i], a[parent-1]
                print("Parent:"+str(parent-1)+" Child:"+str(i))
                i = (i//2)-1
                parent = (parent//2)
                print("parent: " + str(parent-1) + " child:"+str(i))
            else:
                return

    def get_top(self, a):
        heap_size = len(a)
        print("get_top")
        # print(str(heap_size)+" "+str(a[0])+" "+str(a[heap_size-1]))
        a[0], a[heap_size-1] = a[heap_size-1], a[0]
        # print(a[heapsize-1])
        # print(str(heap_size)+" "+str(a[0])+" "+str(a[heap_size-1]))
        # print(a)
        # del a[heap_size-1]
        self.heapify(a, 1, heap_size - 1)
        # build_heap(a, heap_size-1)

    def heap_sort(self, a):
        print("heap_sort")
        heap_size = len(a)
        self.build_heap(a, heap_size)
        while heap_size > 1:
            a[0], a[heap_size-1] = a[heap_size-1], a[0]
            self.heapify(a, 1, heap_size-1)
            heap_size -= 1
            # print(a)

