import pygame
import time


class Model(object):

    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.nodes.append(Node('title',size[0]/2,size[1]/2))
        self.nodes.append(Node('title2',10,0))
        self.clines = []
        self.clines.append(ConnectionLine(self.nodes[0],self.nodes[1]))


class Viewer(object):

    def __init__(self,model):
        self.model = model
        self.screen = pygame.display.set_mode(self.model.size)

    def draw(self):
        self.screen.fill = pygame.Color(0,0,0)
        for node in self.model.nodes:
            pygame.draw.circle(self.screen,pygame.Color(127,127,63),(int(node.x),int(node.y)),node.node_size,10)

class Node(object):

    node_size = 10

    def __init__(self,title,x,y):
        self.x = x
        self.y = y
        self.size = 10

    def __str__(self):
        return '%d,%d' % (self.x,self.y)


class ConnectionLine(object):

    line_length = 10

    def __init__(self,start,end):
        """Start and end are nodes"""
        self.start = start
        self.end = end
        self.x0 = start.x
        self.y0 = start.y
        self.x1 = end.x
        self.y1 = end.y

    def __str__(self):
        return 'Start: %s   End: %s'  % (str(self.start),str(self.end))



if __name__ == '__main__':
    pygame.init()

    node1 = Node('Node1',1,2)
    node2 = Node('Node2',3,4)

    running = True

    view = Viewer(Model((600,400)))
    view.draw()
    k=0
    while k<10 and running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            view.draw()
            time.sleep(.001)
            k=k+1
