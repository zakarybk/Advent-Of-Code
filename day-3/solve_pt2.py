INPUT_FILE = "input.txt"
TREE = '#'

with open(INPUT_FILE, 'r') as f:
	forest = f.readlines()
	forest = [x.strip() for x in forest]


def trees_along_slope(forest, slope):
	forest_width = len(forest[0])
	forest_height = len(forest)

	at_bottom = False
	pos = (0, 0)
	encountered_trees = 0

	while not at_bottom:
		if pos[1] == forest_height - 1:
			at_bottom = True

		square = forest[pos[1]][pos[0]%forest_width]

		if square is TREE:
			encountered_trees += 1

		# x, y
		pos = (pos[0] + slope[0], pos[1] + slope[1])

	return encountered_trees

print(trees_along_slope(forest, (1, 1)))
print(trees_along_slope(forest, (3, 1)))
print(trees_along_slope(forest, (5, 1)))
print(trees_along_slope(forest, (7, 1)))
print(trees_along_slope(forest, (1, 2)))

answer = trees_along_slope(forest, (1, 1))\
		* trees_along_slope(forest, (3, 1))\
		* trees_along_slope(forest, (5, 1))\
		* trees_along_slope(forest, (7, 1))\
		* trees_along_slope(forest, (1, 2))

print("Encrountered " + str(answer) + " trees!")