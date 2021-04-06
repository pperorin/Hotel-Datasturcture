from django.shortcuts import render

class Stack:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def push(self,item):
        self.lst.append(item)
    def pop(self):
        self.lst.pop()
    def peek(self):
        return self.lst[-1]
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def lststack(self):
        return self.lst
    def find(self,num):
        return self.lst[num]

class Queue:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def top(self):
        return self.lst[0]
    def enQ(self,obj):
        self.lst.append(obj)
    def deQ(self):
        return self.lst.pop(0)
    def show(self):
        return self.lst


# Create your views here.
