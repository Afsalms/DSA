


def tower_of_hanoi(n, source, destination, auxilary):
    if n == 1:
        print("Disk:", n, "moved from " , source + " -> " + destination)
    else:
        tower_of_hanoi(n-1, source, auxilary, destination)
        print("Disk:",n, "moved from ",source + " -> " + destination)
        tower_of_hanoi(n-1, auxilary, destination, source)




tower_of_hanoi(3, "A", "C", "B")
