from django.db import models

# Create your models here.
class Cliente(models.Model):
    dni = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    date_joined = models.DateField(auto_now_add=True)
    gender = models.CharField(choices=(('M', 'male'), ('F', 'female')), max_length=1)
def __str__(self):
    return f'{self.name} {self.last_name} {self.dni}'

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def show(self):
        current_node = self.head
        if self.head:
            while current_node:
                print(current_node.data, end=' <- ')
                current_node = current_node.next
        else:
            print('None')


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# material para el proyecto

class LinkedList:
    def __init__(self):
        self.head = None

    #
    def appendend(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def appendstart(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def show(self):
        current_node = self.head
        if self.head:
            while current_node:
                print(current_node.data, end=' <- ')
                current_node = current_node.next
            print('new')
        else:
            print('None')

    def deleteend(self):
        if self.head is None:
            return 'La lista esta vacia'
        self.head = self.head.next

    def deletestart(self):
        if self.head is None:
            return 'la lista esta vacia'
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


"""es"""