from time import sleep

class Employe :
    def __init__ (self, id_employe, name_employe, position, department, salary, join_date) :
        self.id = id_employe
        self.name = name_employe
        self.position = position
        self.department = department
        self.salary = salary
        self.join = join_date 
    
    def display(self):
        print(f'\nID Employe : {self.id}\nEmploye Name: {self.name}\nPosition : {self.position}\nDepartment : {self.department}\nSalary : {self.salary}\nJoin Date : {self.join}\n\n')
        
class Employe_manager :
    
    def __init__ (self) :
        self.Employe_list = []
    
    def add_employe (self) :
        id_employe = input('\nEnter Employe ID : ')
        name_employe = input('Enter Employe Name : ')
        position = input('Enter the Position Employe : ')
        department = input('Department Employe : ')
        salary = input('Enter Salary : ')
        join_date = input('Join Date : ')       
        emp = Employe(id_employe, name_employe, position, department, salary, join_date)
        self.Employe_list.append(emp)
        print('Employe added Successfull!!!')
    
    def delete_employe (self) :
        emp_id = input('Enter the Employe ID : ')
        for emp in self.Employe_list :
            if emp.id == emp_id :
                self.Employe_list.remove(emp)
                print('Successfull remove employe...')
                return
            print('Employe ID not found..')
                
    def display_employe (self) :
        for emp in self.Employe_list :
            emp.display()
                 
manager = Employe_manager()

def back_program ():
    while True :
        back = input('Enter "BACK" with capital for back to menu and "EXIT" with capital for exit : ')
        if back == 'BACK' :
            start()
        elif back == 'EXIT' :
            exit_program()
        else :
            continue 

def exit_program() :
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Exiting the program...')
    exit()
         

def start () :
    menu = int(input('\nWELCOME TO THE BARBER HR MENU!!!\n\n1.Display Employe\n2.Add Employe\n3.Delete Employe\n4.Exit Menu...\n\nPlease chose 1 menu : '))
    if menu == 1 :
        manager.display_employe()
        start()
    elif menu == 2 :
        manager.add_employe()
        start()
    elif menu == 3 :
        manager.delete_employe()
        start()
    elif menu == 4 : 
        exit_program()

        
if __name__ == '__main__' :
    start()    
        
           