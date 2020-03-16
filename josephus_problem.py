import math

def solve_josephus_problem(number):
    highest_power_of_two = int(math.log(number, 2))
    nearest_integer = int(math.pow(2, highest_power_of_two))
    return (number - nearest_integer) * 2 + 1



if __name__ == "__main__":
    try:
        number = int(input("Enter number of seat: \n"))
        winner = solve_josephus_problem(number)
        print(f'Person on {winner} is the winner')
    except:
        print("Invalid input")

