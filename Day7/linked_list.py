import sys
class Node:
    def __init__(self,data=0):
        self.data=data
        self.link=None
        print(f"Node with {data} created")
    
class Linked_List:
    def __init__(self):
        self.first=None
    
    def add_node(self):
        cur=None
        data=int(input("Enter the data of the new node:"))
        node=Node(data)
        if self.first is None:
            self.first=node
            return
        start=node
        cur=start
        while cur.link != None:
            cur=cur.link
        cur.link=node
        return
    
    def add_at_pos(self):
        cur=None
        pos=int(input("Enter the position where data should be inserted:"))
        data=int(input(f"Enter the data of the new node to be inserted at {pos} position:"))
        node=Node(data)
        if pos==1:
            self.link=node
            return
        else:
            start=node
            cur=start
            i=1
            while i < pos:
                cur=cur.link
                i+=1
            node.link=cur.link
            cur.link=node
        return

    def del_at_pos(self):
        cur=None
        pos=int(input("Enter the position where data should be deleted:"))
        if pos==0:
            print(f"Link with data {self.data} deleted")
            return
        else:
            start=node
            cur=start
            i=1
            while i<pos-1:
                cur=cur.link.link
                i+=1
            print(f"Link with data {cur.link.data} deleted")
            cur.link=cur.link.link
        return

    def display(self):
        temp=self.first
        while temp != None:
            print(temp.data)
            temp=self.first.link
    
class Menu:
    def end_of_program(self):
        print("End of Program")
        sys.exit(0)
    
    def invalid_choice(self):
        print("Invalid Choice Entered")
    
    def match_user_choice(self,choice,ll):
        match choice:
            case 1:
                ll.add_node()
            case 2:
                ll.add_at_pos()
            case 3:
                ll.del_at_pos()
            case 4 :
                ll.display()
            case 5 :
                self.end_of_program()
            case _ :
                self.invalid_choice()
    
    def run_menu(self):
        ll=Linked_List()
        while True:
            choice=int(input("1:Add Node 2:Add at Position 3:Delete at Position 4:Display 5:Exit\nEnter your choice:"))
            self.match_user_choice(choice,ll)

def start_app():
    menu=Menu()
    menu.run_menu()

start_app()
            
        

