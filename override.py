#!/usr/bin/python3

class Dog:
    def __init__(self, name):
        self.name = name
        print("Init Dog")
    def bark(self):
        print (self.name + ": WOOF")
    def run(self):
        self.bark()
