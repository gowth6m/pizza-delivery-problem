# Question 2 - Pizzeria Problem

def pizzeria_location_checker(pizzeria_coord, city_size):
    """
    Validates given pizzeria coord
    :param pizzeria_coord: contains 3 integers - x axis, y axis and r represents the maximum distance that the given
    pizzeria's delivery guy will travel to deliver pizza.
    :param city_size: the size of the city as such city_size x city_size
    """
    # Checks if X & Y of given pizzeria coord doesn't exceed city size
    if not ((1 <= pizzeria_coord[0] <= city_size) and (1 <= pizzeria_coord[1] <= city_size)):  # De Morgan
        raise Exception('Pizzeria coordinate outside of valid city range')
    # Checks if R value of given pizzeria coord is in valid range
    if not (1 <= pizzeria_coord[2] <= 100):
        raise Exception('Invalid maximum delivery distance')


def get_input():
    """
    Takes in input from stdin, validates and returns the following
    :return: city size, number of pizzeria in the city, a list containing pizzeria coordinates
    """
    initial_raw_input = input()  # Gets first line of the stdin
    city_size, no_of_pizzerias = initial_raw_input.split()
    city_size, no_of_pizzerias = int(city_size), int(no_of_pizzerias)

    # Checks for valid city size
    if not (1 <= city_size <= 10000):
        raise Exception('Dimension of city not within valid range')
    # Checks for valid city size
    if not (1 <= no_of_pizzerias <= 10000):
        raise Exception('Number of pizzerias not within valid range')

    pizzerias = []
    for i in range(0, no_of_pizzerias):  # Gets the pizzeria coordinates
        single_pizzeria = [int(n) for n in input().split()]
        pizzerias.append(single_pizzeria)
        pizzeria_location_checker(single_pizzeria, city_size)

    return city_size, no_of_pizzerias, pizzerias


def print_matrix(matrix):
    """
    Prints matrix in a 2D format for better visualisation
    :param matrix: a 2D array that represents a matrix
    """
    for row in matrix:
        print(row)


def get_pizzeria_matrix(size, pizzeria_coord):
    """
    Creates a matrix that shows city, where 1s represents area where pizzeria can deliver and 0 is everywhere else.
    :param size: the size of the city
    :param pizzeria_coord: an array containing 3 integers that represents x coordinate, y coordinate and r which
    represents the max delivery distance.
    :return: a 2D array that represents a matrix for a pizzeria
    """
    x = pizzeria_coord[0] - 1
    y = pizzeria_coord[1] - 1
    r = pizzeria_coord[2]

    # Creating a 2D array representing the city matrix
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    # Using max and min here to ensure negative number or a coordinate larger than city size is returned.
    y_min, y_max = max(y - r, 0), min(y + r + 1, size)
    x_min, x_max = max(x - r, 0), min(x + r + 1, size)
    # Only inputs 1 if total absolute value is less than or equal to r to ensure that as i and j increase,
    # the correct range of x and y values are put into the matrix.
    for i in range(y_min, y_max):
        for j in range(x_min, x_max):
            if (abs(i - y) + abs(j - x)) <= r:
                matrix[i][j] = 1
    # Inverting array to get it the same format as example
    matrix = matrix[::-1]
    return matrix


def get_matrix_sum_from_pizzeria_coords(pizzeria_coords, size):
    """
    Takes in a list of pizzeria coordinates, turns them into matrices and calculates the final total matrix
    :param pizzeria_coords: array of pizzeria coordinates
    :param size: the size of the city
    :return: a 2D array representing a total of all matrices coordinates given
    """
    total_matrix = [[0 for _ in range(size)] for _ in range(size)]
    for p in pizzeria_coords:
        for i in range(len(get_pizzeria_matrix(size, p))):
            for j in range(len(get_pizzeria_matrix(size, p)[0])):
                total_matrix[i][j] = total_matrix[i][j] + get_pizzeria_matrix(size, p)[i][j]
    return total_matrix


if __name__ == '__main__':
    file_input = get_input()
    size_of_city = file_input[0]
    number_of_pizzerias = file_input[1]
    all_pizzerias = file_input[2]  # pizzeria coords
    total_m = get_matrix_sum_from_pizzeria_coords(all_pizzerias, size_of_city)
    print_matrix(total_m)
    # print("Max: ", max(max(total_m)))
    print("Max: ", max(max(x) for x in total_m))
