import self as self
class Node:


    def __init__(self, password):
            self.password = password
            self.count = 1
            self.next = None


class DictionaryNode: #class for a dictionary node

    def __init__(self,password, count):
        self.password = password
        self.count = count
        self.next = None

class passList:
    def __init__(self):
        self.head = None
        self.size = 0


    def add(self, password): #adding the new password to the list. As well as checking for any duplicates

        #dummyNode = Node(password)

        if self.head == None: #list is empty

            self.head = Node(password)
            self.size += 1 #size of list

        else:

            curr = self.head

            while(curr != None):

                if curr.password == password: # if the current node's password matches the password passed to the method.

                    curr.count += 1 #increase the amount of times it comes out
                    break

                else:
                    if curr.next == None:

                        curr.next = Node(password) #add a node to list and reference to the previous node
                        self.size +=1
                        break

                curr = curr.next

    def getSize(self):
        return self.size



    def add_to_dictionary(self, node): #function that adds a DictionaryNode into a linkedList

        if self.head == None:

            self.head = DictionaryNode(node.password, node.count)
            self.size +=1

        else:

            curr = self.head

            while(curr.next != None):

                curr = curr.next

            curr.next = DictionaryNode(node.password, node.count)
            self.size += 1


def Dict_insert_node(head, dict):

    while (head != None):

        if head.password in dict:

            dict[head.password] += 1
        else:

            dict[head.password] = 1

        head = head.next





#fills dictionary
def dict_insert(password, dict):

    if password in dict: #if password is in the dictionary

        dict[password] = dict[password] + 1 #add one to the value of the index

    else:

        dict[password] = 1 #else is not in the dictionary so you create an index for it and initialize at 1.


#bubble sort method which sorts the list of passwords
def bubbleSort(list):

    hasSwap = True

    while hasSwap: #boolean flag to check if there has been a swap done
        curr = list.head
        hasSwap = False
        previous = None #variable in order to keep track of the previous node.


        while curr.next != None:

            if curr.count < curr.next.count:
                if previous != None:
                    previous.next = curr.next
                else:
                    list.head = curr.next
                temp = curr.next.next #stores value of curr.next.next
                temp2 = curr.next #stores value of curr.next
                curr.next.next = curr
                curr.next = temp
                previous = temp2  #keeping track of the correct previous
                hasSwap = True


            else:
                previous = curr #update the previous for next iteration
                curr = curr.next #update the curr for next iteration


#adding a Node to the specific index in the dictionary, which has a head which holds the password and the count.
def reference_dictionary(head, dict):

    while(head != None):
        if head.password in dict:
            dict[head.password] = head
        else:
            dict[head.password] = head

        head = head.next

#printing the top 20 passwords
def print_20(head, dict):

    for i in range(0,20,1):
        print("Password:  ", dict[head.password].password, "Counter:  ", dict[head.password].count)
        print("-----------------------------")
        head = head.next


#method to print the list
def prinTop20List(head):

    if head == None:
        return
    for i in range(0,20,1):
        print("Passowrd: ",head.password, "Counter: ", head.count)
        print("-----------------------------")
        head = head.next

def printList(head): #prints top 20 passwords from the dictionary
    if head == None:
        return
    for i in range(0,20,1):
        print(head.password, head.count)
        printList(head.next)


def copy_contents(list, dict): #copies elements in dictionary into a list

    for item, value in dict.items():

        dummy = DictionaryNode(item,value)

        list.add_to_dictionary(dummy)


def merge_sort(head):
    if head == None or head.next == None:

        return head

    left, right = split(head)
    merge_sort(left)
    merge_sort(right)
    merge_lists(left, right)

#returns the left and the right
def split(head):
    previous = None

    if head == None:

        return head
    f1 = head.next
    f2 = head


    while f1 !=  None:
        f1 = f1.next
        if f1 != None:
            f2 = f2.next
            f1 = f1.next

    right = f2.next
    f2.next = None


    return head, right

def merge_lists(left, right):


    if left == None and right == None:

        return None

    if left == None:

        return right

    if right == None:

        return left

    if left.count > right.count:
        result = left
        left = left.next
    else:
        result = right
        right = right.next
    last = result

    while left != None and right != None:

        if left.count > right.count:
            last.next = left
            left = left.next
        else:
            last.next = right
            right = right.next
        last = last.next

    if left != None:
        last.next = left
    elif right !=None:
        last.next = right

    return result




def get_size(head):

    counter = 0

    while head != None:

        counter += 1
        head = head.next

    return counter


def main():


    password_List = passList() #list with the passwords

    dictionary = {}

    dictionary_linked_list = passList() #dictionary values turned into a list

    password_file = open("test.txt", "r")

    #traversing the file
    for line in password_file:
        var = line.rpartition('\t')
        password_List.add(var[2]) #getting the value at index 2 since partition returns 3 values AND inserting it into the password list
        dict_insert(var[2], dictionary)

    password_file.close()

    
    for items in dictionary:
        print(items, dictionary[items])



    bubbleSort(password_List)
    print("---------------------- LINKED LIST BUBBLE SORT ---------------------------")
    prinTop20List(password_List.head)
    copy_contents(dictionary_linked_list, dictionary)
    #printList(dictionary_linked_list.head)
    print("---------------------- DICTIONARY TOP 20 ------------------------------")
    reference_dictionary(password_List.head, dictionary)
    #merge_sort(dictionary_linked_list.head)
    #Dict_insert_node(dictionary_linked_list.head, dictionary)
    print_20(password_List.head,  dictionary)










main()









