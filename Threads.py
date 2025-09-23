class ProcessManagement:
    def __init__(self, name, SID, age):
        self.name = name
        self.SID = SID
        self.age = age

    def printing(self):
        print(self.name, self.SID, self.age)

if __name__ == "__main__":
    Process1 = ProcessManagement('Aidan', '900000000', 21)
    Process2 = ProcessManagement('Tyler', '900000001', 22)

    print("This is for threads")
    Process1.printing()