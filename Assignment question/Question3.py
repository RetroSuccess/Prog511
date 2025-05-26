# The triangle 
for row in range(5):
    num_stars = 2 * row + 1
    num_spaces = (9 - num_stars) // 2
    print(' ' * num_spaces + '* ' * num_stars)
    
# square part
for square_row in range(5):
    if square_row == 4:
        print('  ' + '* ' * 7)
    else:
        # Start with 2 spaces, then star, then 5 empty spaces, then star
        print('  ' + '* ' + '  ' * 5 + '*')


