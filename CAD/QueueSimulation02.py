##Queue simulation
global queue, front, rear, MAX
queue = [0,0,0,0,0,0,0,0]
front = -1
rear = -1
MAX = 2

def insert(element):
    global queue, front, rear, MAX
    if rear == MAX-1 and front == 0:
        print "Queue Full"
        return
    elif rear == front-1:
        print "Queue Full"
        return

    if front == -1:
        front = 0
    elif rear == MAX-1 and front > 0:
        rear = -1

    rear += 1
    queue[rear] = element


def delete():
    global queue, front, rear, MAX
    if front == -1:
        print "Queue is Empty"
        return
    elif front == rear:
        print queue[front],"Has been deleted"
        queue[front] = 0
        front = -1
        rear = -1
        return
    elif front == MAX-1 and rear < front:
        print queue[front],"Has been deleted"
        queue[front] = 0
        front = 0
        return
    
    print queue[front],"Has been deleted"
    queue[front] = 0
    front += 1

def display():
    global queue, front, rear, MAX
    if front == -1:
        print "Queue is Empty"
        return

    if rear < front:
        index = -1
        for i in range(front, MAX, 1):
            index += 1
            print "item[%s] = %s"%(index, queue[i])
        for i in range(0, rear+1, 1):
            index += 1
            print "item[%s] = %s"%(index, queue[i])
        return
    for i in range(front, rear+1, 1):
        print "item[%s] = %s"%(i-front, queue[i])

def display2():
    global queue, front, rear, MAX
    for i in range(0, MAX, 1):
        print "item[%s] = %s"%(i, queue[i])

def queue_is_empty():
    global queue, front, rear, MAX
    if front == -1:
        return True
    else:
        return False

def queue_is_full():
    global queue, front, rear, MAX
    if (rear == MAX-1 and front == 0) or (rear == front-1):
        return True
    else:
        return False

def queue_length():
    global queue, front, rear, MAX
    if queue_is_empty() == True:
        return 0
    elif rear < front:
        length = MAX - front + rear + 1
        return length
    else:
        length = rear-front + 1
        return length

def set_buffer_size(newBufferSize):
    global queue, front, rear, MAX
    if (queue_is_full() and newBufferSize < MAX) or (newBufferSize <= 0):
        print "Queue is Full and bufferSize < MAX || bufferSize <= 0"
        return
    elif newBufferSize < queue_length():
        print "bufferSize < queue_length"
        return
    else:
        MAX = newBufferSize
        print "New Buffer Size =",MAX
        return
    
def main():
    global queue, front, rear, MAX
    if __name__ == "__main__":
        while(1):
            print "Enter your choice"
            print "1. Insert"
            print "2. Delete"
            print "3. Display"
            print "4. Display2"
            print "5. Set Buffer Size"
            print "6. Queue Length"
            print "8. Exit"
            choice = str(raw_input("Choice? "))
            if choice == "1":
                element = str(raw_input("Enter an element to be inserted? "))
                insert(element)
            elif choice == "2":
                element = delete()
            elif choice == "3":
                display()
            elif choice == "4":
                display2()
            elif choice == "5":
                new_length = str(raw_input("Enter new buffer size"))
                try:
                    n = int(new_length)
                    set_buffer_size(n)
                except:
                    print "Invalid Buffer Size"
            elif choice == "6":
                print "Number of elements =",queue_length()
            elif choice == "8":
                exit()
            else:
                print "Invalid Choice"

main()
