l = []


def BubbleSort(showsteps=False):
    if showsteps:
        print(f"step {0}: {l}")
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        if showsteps:
            print(f"step {i+1}: {l}")
    print(f"result: {l}")


def SelectionSort(showsteps=False):
    if showsteps:
        print(f"step {0}: {l}")
    for i in range(len(l)):
        min_index = i
        min_val = l[i]
        for j in range(i+1, len(l)):
            if l[j] < min_val:
                min_index = j
                min_val = l[j]
        l[i], l[min_index] = l[min_index], l[i]
        if showsteps:
            print(f"step {i+1}: {l}")
    print(f"result: {l}")


def InsertionSort(showsteps=False):
    if showsteps:
        print(f"step {0}: {l}")
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
        if showsteps:
            print(f"step {i}: {l}")
    print(f"result: {l}")


def SetList():
    global l
    l = [11, 4, 7, 5, 10, 9, 13, 1]


def main():
    print("1. Bubble Sort")
    print("2. Bubble Sort (show steps)")
    print("3. Selection Sort")
    print("4. Selection Sort (show steps)")
    print("5. Insertion Sort")
    print("6. Insertion Sort (show steps)")
    print("7. Exit")
    while True:
        choice = input("\nEnter your choice: ")
        print()
        if choice == "1":
            SetList()
            BubbleSort()
        elif choice == "2":
            SetList()
            BubbleSort(True)
        elif choice == "3":
            SetList()
            SelectionSort()
        elif choice == "4":
            SetList()
            SelectionSort(True)
        elif choice == "5":
            SetList()
            InsertionSort()
        elif choice == "6":
            SetList()
            InsertionSort(True)
        elif choice == "7":
            break
        else:
            print("Invalid choice")


main()