INPUT_FILE = "input.txt"
TREE = '#'

with open(INPUT_FILE, 'r') as f:
	forest = f.readlines()
	forest = [x.strip() for x in forest]

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
	pos = (pos[0] + 3, pos[1] + 1)

print("Encrountered " + str(encountered_trees) + " trees!")