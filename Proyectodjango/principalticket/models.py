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

