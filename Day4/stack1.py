import sys
class Stack:
    def __init__(self,size=5):
        self.stack=[]
        self.size=size
        print("Empty Stack Created")
    def push(self):
        if len(self.stack)==self.size:
            print("Stack Overflow")
            return
        element=input("Enter the element to be pushed")
        self.stack.insert(0,element)
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        print("Popped Element is ",self.stack[0])
        del self.stack[0]
    def display(self):
        if not self.stack:
            print("Stack is Empty")
            return
        print("Stack:",self.stack)
class Menu:
    def __init__(self):
        pass
    def get_menu(self,stack):
        menu={1:stack.push,2:stack.pop,3:stack.display,4:self.end_of_program}
        return menu
    def end_of_program(self):
        print("End of Program")
        sys.exit(0)
    def invalid_choice(self):
        print("Invalid Choice Entered")
    def run_menu(self):
        stack=Stack()
        while True:
            choice=int(input("1:Push 2:Pop 3:Display 4.Exit\nEnter your choice:"))
            menu=self.get_menu(stack)
            menu.get(choice,self.invalid_choice)()
menu=Menu()
menu.run_menu()