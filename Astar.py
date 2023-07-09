from tkinter import messagebox, Tk
import pygame
import sys
import heapdict
  
pq = heapdict.heapdict()

win_width = 800
win_height = 800

window = pygame.display.set_mode((win_width, win_height))





class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.distance=-1
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None
        self.diagonal=False

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width-2, box_height-2))

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])
        
       
        #diagonal
        if self.x+1<=columns-1 and self.y+1<=rows-1:
            grid[self.x+1][self.y+1].diagonal=True
            self.neighbours.append(grid[self.x+1][self.y+1])
        if self.x+1<=columns-1 and self.y-1>0:
            grid[self.x+1][self.y-1].diagonal=True
            self.neighbours.append(grid[self.x+1][self.y-1])
        if self.x-1>0 and self.y+1<=rows-1:
            grid[self.x-1][self.y+1].diagonal=True
            self.neighbours.append(grid[self.x-1][self.y+1])
        if self.x-1>0 and self.y-1>0:
            grid[self.x-1][self.y-1].diagonal=True
            self.neighbours.append(grid[self.x-1][self.y-1])

        

    def set_distance(self, box_obj):
       if not self.diagonal:
        self.distance=((self.x-box_obj.x)**2+(self.y-box_obj.y)**2)**0.5
       else:
        self.distance=0.05+((self.x-box_obj.x)**2+(self.y-box_obj.y)**2)**0.5

    

            

columns = 25
rows = 25

box_width = win_width // columns
box_height = win_height // rows


                
grid = []
path = []            




for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)


start_box = grid[0][0]
start_box.start = True
start_box.visited = True
pq[start_box]=start_box.distance

def main():
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
               
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    grid[i][j].wall = True
               
                if event.buttons[2] and not target_box_set:
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
            
            if event.type == pygame.KEYUP and target_box_set:
                begin_search = True
       
                                    
        if begin_search:
            if len(pq.items())>0 and searching:
                (current_box, d) = pq.peekitem()
                pq.popitem()
                current_box.visited = True
                current_box.set_neighbours()
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    flag=0
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall and not flag:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            neighbour.set_distance(target_box)
                            pq[neighbour]=neighbour.distance
                            if(neighbour==target_box):
                             flag=1

                            
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There is no solution!")
                    searching = False

        window.fill((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (100, 100, 100))

                if box.queued:
                    box.draw(window, (225, 0, 0))
                if box.visited:
                    box.draw(window, (0, 225, 0))
                if box in path:
                    box.draw(window, (0, 0, 225))

                if box.start:
                    box.draw(window, (0, 200, 200))
                if box.wall:
                    box.draw(window, (10, 10, 10))
                if box.target:
                    box.draw(window, (200, 200, 0))

        pygame.display.flip()


main()
