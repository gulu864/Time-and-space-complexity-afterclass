def count_ways(rupees, notes, index):
    if rupees == 0:
        return 1

    if rupees < 0 or index >= len(notes):
        return 0
    
    ways = 0
    note = notes[index]

    for i in range(rupees // note + 1):
        ways += count_ways(rupees - i * note, notes, index + 1)

    return ways

notes = [500, 100, 10, 5, 1]
rupees = int(input("Enter an amount: "))
print("Number of ways:", count_ways(rupees, notes, 0))
