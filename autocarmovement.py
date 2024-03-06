from enum import Enum

#Enums for Directions
class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

flag=0 #flag used for simulation purpose
carobjlst=[] #list to hold car objects

#class car to hold car details 
class Car:
    def __init__(self,name,a,b,d,path):
        self.carname=name
        self.curr_x=a
        self.curr_y=b
        self.curr_dir=d
        self.simulate_x=a
        self.simulate_y=b
        self.dir=d
        self.pathway=[]
        self.path=path
    #function to calculate simulation path
    def move(self,path):
        # Find current move
        move = path
        # If move is left or right, then change direction
        if move == 'R':
            self.dir = (self.dir + 1)%4
        elif move == 'L':
            self.dir = (4 + self.dir - 1)%4
 
        # If move is F, then change x or y accordingly
        else:
            if self.dir == Direction['N'].value:
                self.simulate_y+=1
                self.pathway.append((self.simulate_x,self.simulate_y))
            elif self.dir == Direction['E'].value:
                self.simulate_x+=1
                self.pathway.append((self.simulate_x,self.simulate_y))
            elif self.dir == Direction['S'].value:
                self.simulate_y -= 1
                self.pathway.append((self.simulate_x,self.simulate_y))
            else:
                self.simulate_x -= 1
                self.pathway.append((self.simulate_x,self.simulate_y))
    def __str__(self):
        return ("Your current list of cars are :"
                       f" - {self.carname}, ({self.curr_x},{self.curr_y})" 
                       f" {Direction(self.curr_dir).name}, {self.path}\n")

#Function to simulate car movement
def executesimulation(boundary_x,boundary_y):
    dt={}#dictionary used to store mid coordinates during simulation
    i=0
    k=0
    if len(carobjlst)==0:
        print("No car details to simulate\n")
        exit()

    #loop will execute untill all car objects movements are simulated
    while True: 
        
        #check to execute till car path length
        if k<len(carobjlst[i].path):
            
            #call move method for each command in car path
            carobjlst[i].move(carobjlst[i].path[k])
            
            #code to check boundary check          
            if(carobjlst[i].path[k]=='F'):
                if(carobjlst[i].simulate_x < 0 or \
                    carobjlst[i].simulate_y > int(boundary_x) or \
                    carobjlst[i].simulate_y < 0 or \
                    carobjlst[i].simulate_y > int(boundary_y)):
                    print(f"{carobjlst[i].carname} moves beyond boundaries"
                          f" at ({carobjlst[i].simulate_x}"
                          f" {carobjlst[i].simulate_y})\n")
                    return False
                
                #code to check collision among cars
                tp=(carobjlst[i].simulate_x,carobjlst[i].simulate_y)
                if tp not in dt.values():
                    dt[carobjlst[i].carname]=tp
                else:
                    print(f"{carobjlst[i].carname} Car collides at {tp} at"
                          f" step {k+1}")
                    return False
            flag=1
        i+=1
        
        #break from WHILE loop if executed all commands for Car objects
        if flag==0:
            break
        #check to loop car objects alternatively
        if i==len(carobjlst):
            i=0
            k+=1
            flag=0
    return True

#function to display car details
def displaycardetails():
    #loop through each object in the list
    for i in range(len(carobjlst)):
        ob=carobjlst[i]
        print(str(ob))
        print("After simulation the result is:"
                        f"- {ob.carname}, ({ob.simulate_x},{ob.simulate_y})"
                        f" {Direction(ob.dir).name}\n")

#function to add car details
def addcardetails():
    carname=input("Please enter the name of the car:")
    #curr_x,curr_y,dir=input("Please enter the initial position of car "
    #            f"{carname} in the x y Direction (Eg: 1 2 N ) format: ").split()
    try:
        #current position,direction    
        curr_x,curr_y,dir=input("Please enter the initial position of car "
                f"{carname} in the x y Direction (Eg: 1 2 N ) format: ").split()
        Direction[dir]
    except ValueError:
        print("\n***Please enter input in valid format(Eg: 1 2 N) ***\n")
        return
    except KeyError:
        print("\n***Please enter valid direction***\n")
        return

    path=input(f"Please enter the commands (Eg: FFRL) for car {carname}: ")
    
    #create car object
    ob=Car(carname, int(curr_x), \
           int(curr_y),Direction[dir].value,path)

    #Append carobject in the list
    carobjlst.append(ob)
    
    #loop through carobject list to display added car details
    for i in range(len(carobjlst)):
        ob=carobjlst[i]
        print("\nYour current list of cars are :" 
                f"- {ob.carname}, ({ob.curr_x},{ob.curr_y})"
                f"  {Direction(ob.dir).name}, {ob.path}\n")

#function to process input
def inputprocessing():

    print("\n***Welcome to the Auto Driving Car Simulation!***\n")

    boundary_x,boundary_y=input("Please enter the width and height of the "
                    "simulation field in x,y (Eg: 10,10) format: ").split(',')

    print(f"\nYou have created a field of {boundary_x}*{boundary_y}\n")
    try:
        while True:
            print("""Please Choose from the following options:
                [1] Add a car to field
                [2] Run Simulation\n""")

            option=int(input())
            match option:
                case 1: #Add car details
                    addcardetails()
                    continue

                case 2: #Run simulation
                    ret = executesimulation(boundary_x,boundary_y)
                    #display cardetails function wont get called for collision
                    # and crossing boundary scenarios
                    if ret:
                        displaycardetails()

                    print("""Please Choose from the following options:
                            [1] Start over
                            [2] Exit""")

                    op=int(input())

                    match op:
                        case 1 :
                            carobjlst.clear()
                            continue
                        case 2:
                            exit()
                        case _:
                            print("Enter valid option")
                            exit()
                case _:
                    print("Enter valid option")
                    #exit()

    except :
        exit()

if __name__ == '__main__':
    inputprocessing()
