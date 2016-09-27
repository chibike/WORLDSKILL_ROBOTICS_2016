##Queue simulation
global queue, front, rear, MAX
queue = [0,0,0,0,0]
front = -1
rear = -1
MAX = 5

def insert(element):
    global queue, front, rear, MAX
    if rear == MAX-1:
        print "Queue Full"
        return

    if front == -1:
        front = 0

    rear += 1
    queue[rear] = element


def delete():
    global queue, front, rear, MAX
    if front == -1 or front == rear+1:
        print "Queue is Empty"
        return
    front += 1
    print queue[front-1],"Has been deleted"

def display():
    global queue, front, rear, MAX
    if front == -1 or front == rear+1:
        print "Queue is Empty"
        return

    for i in range(front, rear+1, 1):
        print "item[%s] = %s"%(i-front, queue[i])

def main():
    global queue, front, rear, MAX
    if __name__ == "__main__":
        while(1):
            print "Enter your choice"
            print "1. Insert"
            print "2. Delete"
            print "3. Display"
            print "4. Exit"
            choice = str(raw_input("Choice? "))
            if choice == "1":
                element = str(raw_input("Enter an element to be inserted? "))
                insert(element)
            elif choice == "2":
                element = delete()
            elif choice == "3":
                display()
            elif choice == "4":
                exit()
            else:
                print "Invalid Choice"

main()
