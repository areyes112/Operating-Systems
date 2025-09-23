import threading
import time
class ProcessManagement:
    def __init__(self, name, SID, age):
        self.name = name
        self.SID = SID
        self.age = age

    def printing(self):
        print(self.name, self.SID, self.age)

if __name__ == "__main__":
    #Variable assignment
    Process1 = ProcessManagement('Aidan', '900000000', 21)
    Process2 = ProcessManagement('Tyler', '900000001', 22)
    #Thread assignment
    thread1 = threading.Thread(target=Process1.printing)
    thread2 = threading.Thread(target=Process2.printing)
    #Starting threads
    thread1.start()
    thread2.start()
    #Joining threads
    thread1.join()
    thread2.join()
    #Checking if threads are completed
    print("Threading completed")
