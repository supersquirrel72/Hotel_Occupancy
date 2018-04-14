# Gabriel Winkler
# April 7 - 13th, 2018
# This program will calculate the occupancy rate of a hotel
# based on the number of floors, empty rooms, and occupied rooms.

#imports

# Functions

def getFloors(floors):
    floors = int(input("How many floors are in your hotel?"))
    while floors < 1:
        floors = int(input("Try again. Enter a number above 0."))
    return floors

def getOccupied(floors, rooms, takenRooms, totalRooms, occupiedRooms):
    for x in range(1,floors+1):
        rooms = int(input("How many rooms are on floor " + str(x) + "?"))
        while rooms < 1 or rooms > 100:
            print("You have entered an invalid number.")
            rooms = int(input("Please enter a number between 1 and 100."))
        takenRooms = int(input("How many of these rooms are occupied?"))
        totalRooms = totalRooms + rooms
        occupiedRooms = occupiedRooms + takenRooms
    return totalRooms, occupiedRooms

def calcRate(occupiedRooms, totalRooms):
    occupancyRate = (occupiedRooms / totalRooms) * 100
    return occupancyRate

def printResults(totalRooms, occupiedRooms, emptyRooms, occupancyRate):
    print("Number of rooms in the hotel: " + str(totalRooms))
    print("Number of occupied rooms: " + str(occupiedRooms))
    print("Number of vacant rooms: " + str(emptyRooms))
    print("Occupancy rate: %4.2f" % occupancyRate + "%")

def main():
    floors = 0
    rooms = 0
    takenRooms = 0
    totalRooms = 0
    occupiedRooms = 0

    print("     Welcome to the hotel occupancy rate calculator!")
    print(" I will calculate your occupancy rate based on the number of")
    print(" floors, number of rooms per floor, and number of occupied")
    print(" rooms per floor.")

    floors = getFloors(floors)
    totalRooms, occupiedRooms = getOccupied(floors, rooms, takenRooms, totalRooms, occupiedRooms)
    
    emptyRooms = totalRooms - occupiedRooms

    occupancyRate = calcRate(occupiedRooms, totalRooms)    

    printResults(totalRooms, occupiedRooms, emptyRooms, occupancyRate)    

# Call for main
main()
