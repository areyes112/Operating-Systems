import threading
import time
#ProcessManagement class: Manages processes with attributes and methods
class ProcessManagement:
    def __init__(self, name, SID, age, delay):
        self.name = name
        self.SID = SID
        self.age = age
        self.delay = delay
    #Method to print process details
    def printing(self):
        print(self.name, self.SID, self.age, "\n")

    #Method to simulate studying with delays
    def study(self):
        for i in range(5):
            print(f"{self.name} has studied for {i+1} hours\n")
            time.sleep(self.delay)
        print(f"{self.name} has finished studying\n")
        
    #Method to simulate taking a break
    def take_break(self):
        break_duration = 3
        print(f"{self.name} is taking a {break_duration} minute break\n")
        for minute in range(break_duration):                                
            print(f"{self.name} - break minute {minute + 1}\n")
            time.sleep(1)  
        print(f"{self.name} has finished their break and is refreshed!\n")

#Main execution block: Creating processes and managing threads
if __name__ == "__main__":
    #Variable assignment: Creating instances of ProcessManagement
    Process1 = ProcessManagement('Aidan', '900000000', 21, 2)
    Process2 = ProcessManagement('Tyler', '900000001', 22, 3)
    #Thread assignment: Creating threads for each process
    thread1 = threading.Thread(target=Process1.printing)
    thread2 = threading.Thread(target=Process2.printing)
    thread3 = threading.Thread(target=Process1.study)
    thread4 = threading.Thread(target=Process2.study)

    #Starting threads: Beginning execution of threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


    #Joining threads: Waiting for threads to complete before moving on
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    #Checking if threads are completed
    print("Threading completed")
