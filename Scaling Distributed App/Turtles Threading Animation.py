
from turtle import * #turtle graphics - geometric drawing tools and graphics objects
from threading import Thread #parallelism based on threads interfaces (multiprocessing)
import queue #multi-producer, multi-consumer queues
import random

#/////////////////////////////////////////////////////////////////////////////// MULTIPROCESSING 
QUEUE_SIZE = 2  # number of hardware threads you want to use
ACTIONS = [Turtle.forward, Turtle.right, Turtle.left] #movements for the animations
COLORS = ['red', 'black', 'blue', 'green', 'magenta', 'orange'] #colors of the animations

class RandomTurtle(Thread):
    def __init__(self, turtle, actions):
        super().__init__()
        self.turtle = turtle  #turtle object
        self.actions = actions  #queue with movements
        self.movements = 40

    def run(self):
        for _ in range(self.movements):  #iteration with the number of movements 
            #puts in the queue a TURTLE, its movement, length of move
            self.actions.put((self.turtle, random.choice(ACTIONS), random.randint(1, 30))) 

class MultiProcessing:
    def __init__(self) -> None:
        self.actions = queue.Queue(QUEUE_SIZE) #constructor for a FIFO queue, assigns the number of items that can be placed in the queue

    def createTurtles(self):
        self.screen = Screen() #graphics object that allows multiple turtle objects in the same screen at once
        i = 0

        for color in COLORS:  #for each color creates a TURTLE object, names it and set the initial heading angle
            turtle = Turtle('turtle') #create a Turtle object
            turtle.color(color)       
            turtle.setheading(random.randint(0, 360)) #set the initial orientation of the object
            RandomTurtle(turtle, self.actions).start()  #pass the TURTLE and the actions it could make and runs it in a thread

    def process_queue(self):
        TurtleScreen._RUNNING=True  #this keeps the instance alive avoiding terminating errors
        self.createTurtles() #create all the Turtle objects

        while not self.actions.empty(): #while the queue isn't empty, the processes will execute
            turtle, action, argument = self.actions.get() #gets from queue the next movement for a TURTLE, its movement and length of move
            action(turtle, argument) #action = movement, gives to the movement function the turtle and length of move

        self.screen.mainloop() #the graphics will iterate as long as there are functions running


#///////////////////////////////////////////////////////////////////////////////MAIN
if __name__ == '__main__':

    MP = MultiProcessing() #Multiprocessing class that creates multiple TURTLES 
    MP.process_queue() #starts the animation

    #release the resources from the threading process, this avoid errors with the turtle instance
    TurtleScreen._RUNNING=False 