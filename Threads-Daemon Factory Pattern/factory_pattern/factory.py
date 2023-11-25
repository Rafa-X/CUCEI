from abc import ABC, abstractmethod

import tkinter
from tkinter import ttk

from progress.bar import ChargingBar
import time, random

'''
factory design pattern
'''
class FactoryClass:
    '''
    Factory Class
    '''
    # return the request class messages
    @staticmethod
    def get_class(class_name):
        if class_name == "thread_number_1":
            return Thread_1()
        if class_name == "thread_number_2":
            return Thread_2()
        
        assert 0, 'Could not find shape ' + class_name

'''
Interface - all the class that inherit from this interface must declare methods.
'''
class FactoryInterface(ABC):
    '''
    Messages Interface
    '''
    @abstractmethod
    def run(self): pass
    
'''
methods
'''
class Thread_1(FactoryInterface):
    def __init__(self):
        pass

    def run(self):
        while(True):
            window = tkinter.Tk()
            window.title("Thread 1 with TK")
            window.geometry("300x200")
            progressbar = ttk.Progressbar(mode="indeterminate")
            progressbar.place(x=30, y=60, width=200)
            # Begins the infinite bar movement
            progressbar.start()
            window.mainloop()

    
class Thread_2(FactoryInterface):
    def __init__(self):
        pass

    def run(self):
        while(True):
            bar = ChargingBar('Thread 2 with Progress:', max=100)
            for num in range(100):
                time.sleep(random.uniform(0, 0.2))
                bar.next()
            bar.finish()