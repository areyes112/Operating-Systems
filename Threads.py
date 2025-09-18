class ProcessManagement:
    def init(self, name, SID, age):
        self.name = name
        self.SID = SID
        self.age = age
    
    def printing(self):
        print(Process1.name, Process1.SID, Process1.age)

if __name__ == "__name__":
    Process1 = ('Aidan', '900000000', 21)
    Process2 = ('Tyler','900000001', 22 )

    print("This is for threads")

    print(Process1.printing())