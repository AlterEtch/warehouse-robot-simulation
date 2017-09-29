class RobotAgent():
    def __init__(self, canvas, size=40, pos=[1,1]):
        self.pos = pos
        self.canvas = canvas
        self.size = size
        self.id = self.canvas.create_oval(self.pos[0]*self.size, self.pos[1]*self.size, (self.pos[0]+1)*self.size, (self.pos[1]+1)*self.size, fill="green")

    def move(self, direction, possibleActions=[[0,0],[1,0],[0,1],[-1,0],[0,-1]]):
        if direction in possibleActions:
            self.pos[0] += direction[0]
            self.pos[1] += direction[1]
            self.canvas.move(self.id, direction[0]*self.size, direction[1]*self.size)
        print self.pos

    #def sucessor(self, layout):
