def draw_house():
    # Draw the roof (width must match base = 9 characters)
    for i in range(5):
        stars = 2 * i + 1
        spaces = 4 - i  # 4 spaces for the top line, decreasing
        print(' ' * spaces + '*' * stars + ' ' * spaces)

    # Draw the walls (height = 3, width = 9)
    for i in range(3):
        print('*' + ' ' * 7 + '*')

    # Draw the base
    print('*' * 9)

# Call the function to draw the house
draw_house()



