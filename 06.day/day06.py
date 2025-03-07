import numpy as np
import time

class guardc:
    def __init__(self, map_game, dir_symb, position, X_count):
        self.compass = {
                    'up' : (-1,0), 
                    'right' : (0, 1),
                    'down' : (1,0), 
                    'left' : (0,-1)
                   }
        self.compass_r = {
                    (-1,0):'up', 
                     (0, 1) : 'right',
                     (1,0) : 'down', 
                     (0,-1) : 'left'
                   }
        self.map_game = map_game
        self.dir = self.compass[dir_symb]
        self.position = list(position)
        self.X_count = X_count
        self.history = []
        pass
    
    def get_history(self):
        return self.history
    
    def get_position(self):
        return self.position
    
    def get_dir(self):
        return self.dir
    
    def get_X_count(self):
        unique, frequency = np.unique(self.map_game, 
                              return_counts = True)
        return unique, frequency
    
    def set_val(self, val):
        self.val = val
        
    def obstacle(self):
        if self.map_game[self.position[0] + self.dir[0]][self.position[1] + self.dir[1]] == '#':
            return True  
        return False
    
    def turn_90(self):
        match self.compass_r.get(self.dir):
            case 'up':
                self.dir = self.compass.get('right')
            case 'right':
                self.dir = self.compass.get('down')
            case 'down':
                self.dir = self.compass.get('left')
            case 'left':
                self.dir = self.compass.get('up')
    
    def step_forward(self):
        self.position[0] += self.dir[0]
        self.position[1] += self.dir[1]
        self.history.append(self.position)
        pass
    
    def put_X(self):
        if self.grab_map() != 'X':
            self.map_game[self.position[0]][self.position[1]] = 'X' 
            self.X_count += 1 
        #print(self.map_game[self.position[0] - 5:self.position[0] + 5, self.position[1] - 5 : self.position[1] + 5])
        #print('\n')
        #time.sleep(1)

    def grab_map(self):
        return self.map_game[self.position[0]][self.position[1]]

    def run_guard(self):
        while self.grab_map() != '0':   #algorithm works up untill guard is holding '0' padding which means map area is over
            self.put_X()
            if self.obstacle():        #if guard sees '#' in direction of moving, he turns
                self.turn_90()
            if not self.obstacle():
                self.step_forward()    #guard makes 1 step in his direction of standing and puts 'X' to his previous position
                

with open('data.txt', 'r') as f:
    data = np.asarray([list(el) for el in f.read().split()])

map_game = np.pad(data[:], pad_width=1, constant_values=0)
position = list(map(int, np.where(map_game == '^')))
print(map_game, type(map_game), type(position))

val = 'X'
X_count = 0
dir_symb = 'up'
guard = guardc(map_game, dir_symb,position, X_count)

guard.run_guard()
""" 
while guard.grab_map() != '0':   #algorithm works up untill guard is holding '0' padding which means map area is over
    guard.put_X()
    if guard.obstacle():        #if guard sees '#' in direction of moving, he turns
        guard.turn_90()
    if not guard.obstacle():
        guard.step_forward()    #guard makes 1 step in his direction of standing and puts 'X' to his previous position
        
 """
        
print(guard.get_X_count())
        
