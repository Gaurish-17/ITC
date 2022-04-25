color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("The provided list is ", color, '\n')

# removing the 4th term and returning modified list
color.pop(3)
print(" The modified list  is color 1 =", color)

# replacing 'Black' and 'Pink' with 'Purple'
color2 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color2[3:5] = ['Purple']
print("The modified list is color 2 =", color2)
