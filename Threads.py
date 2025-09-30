import threading 
import time
class ProcessManagement: #Class to manage process details and actions
    def __init__(self, name, SID, age, delay): #Constructor to initialize process attributes
        self.name = name #Attributes for process details
        self.SID = SID #Attributes for process details
        self.age = age #Attributes for process details
        self.delay = delay #Delay attribute for simulating study time

    #Method to print process details
    def printing(self): #Prints the process details
        print(self.name, self.SID, self.age, "\n") 
        printing_done.set() #Signal that printing is done

    #Method to simulate studying with delays
    def study(self): 
        printing_done.wait() #Ensures printing is done before studying
        for i in range(5): #Simulates studying for 5 hours
            print(f"{self.name} has studied for {i+1} hours\n") 
            time.sleep(self.delay) #Simulates delay for each hour of study
        print(f"{self.name} has finished studying\n") 
        study_done.set() #Signal that studying is done
    #Method to simulate taking a break
    def take_break(self):
        study_done.wait() #Ensures studying is done before taking a break
        break_duration = 3 # Duration of the break in minutes
        print(f"{self.name} is taking a {break_duration} minute break\n") 
        for minute in range(break_duration): #Simulates each minute of the break                                
            print(f"{self.name} - break minute {minute + 1}\n") 
            time.sleep(1) # Simulates 1 second per minute of break
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
    thread5 = threading.Thread(target=Process1.take_break)
    thread6 = threading.Thread(target=Process2.take_break)

    #Starting threads: Beginning execution of threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()


    #Joining threads: Waiting for threads to complete before moving on
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    #Checking if threads are completed
    print("Threading completed")
