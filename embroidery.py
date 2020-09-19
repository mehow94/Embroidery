def draw_rectangle(width, height, border_width=1, border_color=1, fill_color=1):
    matrix = []

    for i in range(height):
        row_list = []

        if i < border_width or i >= height - border_width:
            for j in range(width):
                row_list.append(border_color)
            matrix.append(row_list)
        else:
            for j in range(width):
                if j < border_width or j >= width - border_width:
                    row_list.append(border_color)
                else:      
                    row_list.append(fill_color)
            matrix.append(row_list)

    return matrix


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
    return matrix


def draw_circle(radius):
    matrix = []
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    # embroider([
    #     [0, 0, 0, 1, 0, 0, 0], 
    #     [0, 0, 1, 2, 1, 0, 0], 
    #     [0, 1, 2, 2, 2, 1, 0], 
    #     [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    my_border_color = 3
    embroider(draw_rectangle(9, 10, border_width=2,border_color=2, fill_color=0), color_scheme)
