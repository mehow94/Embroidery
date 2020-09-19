import math
import sys

def draw_rectangle(width, height, border_width=1, border_color=1, fill_color=1):
    matrix = []

    for i in range(height):
        row = []

        if i < border_width or i >= height - border_width:
            for j in range(width):
                row.append(border_color)
            matrix.append(row)
        else:
            for j in range(width):
                if j < border_width or j >= width - border_width:
                    row.append(border_color)
                else:      
                    row.append(fill_color)
            matrix.append(row)

    return matrix


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks, border_color = 1, fill_color = 1, empty_color = 0, block_height = 3):
    matrix = []
    block_width = 3 + 2 * blocks

    for block_number in range(blocks):
        for i in range(block_height):
            row = []
            for j in range(block_width):
                if j < i + block_number  or j >= block_width - i - block_number:
                    row.append(empty_color)
                else:
                    if (j < i + block_number + 1 or
                        j >= block_width - i - block_number -1 or
                        (block_number == 0 and i == 0)):
                        row.append(border_color)
                    else:
                        row.append(fill_color)

            matrix.append(row)
    matrix.reverse()
    return matrix


def draw_circle(radius):
    matrix = []

    diameter = 2 * radius
    empty_color = 0
    fill_color = 1
    for i in range(diameter):
        row = []
        for j in range(diameter):
            if is_inside(j, i, radius):
                row.append(fill_color)
            else:
                row.append(empty_color)
        matrix.append(row)
    return matrix


def is_inside(j, i, radius):
    if math.pow(j-radius,2) + math.pow(i-radius,2) < math.pow(radius,2):
        return True
    else:
        return False


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()

def no_color_embroider(matrix):
    for row in matrix:
        for cell in row:
            print(cell," ", end='')
        print()
    print()

def save_to_file(matrix, filename="output.txt", color_scheme = {0: 0, 1: 1, 2: 2, 3: 3}):
    with open(filename, "w+") as file_to_wrtie:
        for row in matrix:
            for cell in row:
                file_to_wrtie.write(str(color_scheme[cell]))
            file_to_wrtie.write("\n")
        file_to_wrtie.write("\n")




if __name__ == '__main__':
    print(sys.argv)
    # embroider([
    #     [0, 0, 0, 1, 0, 0, 0], 
    #     [0, 0, 1, 2, 1, 0, 0], 
    #     [0, 1, 2, 2, 2, 1, 0], 
    #     [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # my_border_color = 3
    # embroider(draw_rectangle(9, 10, border_width=2,border_color=2, fill_color=0), color_scheme)

    blocks = 5
    if len(sys.argv) >= 3:
        blocks = int(sys.argv[2])

    color_scheme = {0: ' ', 1: '*', 2: '.'}
    if len(sys.argv) >= 4:
        if sys.argv[3] == '--color':
            color_scheme = {0: ' ', 1: '\033[93m*\033[0m', 2: '\033[92m.\033[0m'}



    if sys.argv[1] == '--print':
        embroider(draw_christmas_tree(blocks, fill_color=2), color_scheme=color_scheme)
    
    if sys.argv[1] == '--save':
        save_to_file(draw_christmas_tree(blocks, fill_color=2), color_scheme=color_scheme)
    #embroider(draw_christmas_tree(6,border_color=1,fill_color=2), color_scheme)

    #no_color_embroider(draw_circle(15))

