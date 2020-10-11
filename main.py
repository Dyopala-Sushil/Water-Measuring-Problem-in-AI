#Python script for die hard water puzzle or water jug problem or measurement problem in AI

class DieHardWaterPuzzle():
    def __init__(self,x=0,y=0,xsize = 7, ysize = 5, desiredVolume=6, max_iter=20):
        self.x = x   #current state of larger container
        self.y = y   #current state of smaller container
        self.xsize = xsize   #capacity of larger container
        self.ysize = ysize   #capacity of smaller container
        self.desiredVolume = desiredVolume   #volume to be measured
        self.solution_states = [(0,0)]   #list containing all the solution sates
        self.max_iter = max_iter

    #pour water from lager container to smaller container
    def pour(self):
        temp = self.y
        self.y = self.y + self.x
        self.x = self.x - (self.ysize - temp)
        if self.y > self.ysize:
            self.y = self.ysize
        if self.x < 0:
            self.x = 0

    #make the container empty
    def empty(self):
        return 0

    #fill up the larger container
    def fillx(self):
        self.x = self.xsize

    #fill up the smaller container
    def filly(self):
        self.y = self.ysize

    #check if the present state is goal sate or not
    def GoalCheck(self):
        for x,y in self.solution_states:
            if self.desiredVolume ==x:
                self.solution_states.append((x,self.empty()))
                return True
        return False

    #recursion to find all the sates to the goal state
    def GoalFinder(self):
        self.max_iter-=1
        if self.GoalCheck() :
            return True

        #fill x
        self.fillx()
        self.solution_states.append((self.x,self.y))
        if self.GoalCheck() :
            return True

        #pour x-->y
        self.pour()
        self.solution_states.append((self.x,self.y))        
        if self.GoalCheck() :
            return True

        #empty y and pour x-->y
        self.y = self.empty()
        self.pour()
        self.solution_states.append((self.x,self.y))
        if self.GoalCheck() :
            return True

        if self.max_iter==0:
            return False

        if self.GoalFinder():
            return True
        
    
if __name__ == "__main__":
    xsize = int(input("Enter the size of bigger container :"))
    ysize = int(input("Enter the size of smaller container : "))
    desiredVolume = int(input("Enter the desired volume : "))

    puzzle = DieHardWaterPuzzle(xsize=xsize, ysize=ysize, desiredVolume=desiredVolume, max_iter=30)
    if puzzle.GoalFinder():
        print("\nSolution States :\n")
        for i,item in enumerate(puzzle.solution_states):
            print(f"State {i} : {item} ")
    else:
        print("Solution Not Found")
    




