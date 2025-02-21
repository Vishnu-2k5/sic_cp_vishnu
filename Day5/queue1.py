import sys
class Queue:
    def __init__(self,size=5):
        self.queue=[]
        self.size=size
        print("Empty Queue Created")
    def push(self):
        if len(self.queue)==self.size:
            print("Queue Overflow")
            return
        element=input("Enter the element to be pushed")
        self.queue.insert(0,element)
    def pop(self):
        if not self.queue:
            print("Queue Underflow")
            return
        print("Popped Element is ",self.queue[-1])
        del self.queue[-1]
    def display(self):
        if not self.queue:
            print("Queue is Empty")
            return
        print("Queue:",self.queue)
class Menu:
    def __init__(self):
        pass
    def get_menu(self,queue):
        menu={1:queue.push,2:queue.pop,3:queue.display,4:self.end_of_program}
        return menu
    def end_of_program(self):
        print("End of Program")
        sys.exit(0)
    def invalid_choice(self):
        print("Invalid Choice Entered")
    def run_menu(self):
        queue=Queue()
        while True:
            choice=int(input("1:Push 2:Pop 3:Display 4.Exit\nEnter your choice:"))
            menu=self.get_menu(queue)
            menu.get(choice,self.invalid_choice)()
menu=Menu()
menu.run_menu()