grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

def gridprint(listName):
    import copy
    printGrid = copy.deepcopy(listName)
    height = len(printGrid[0])
    width = len(printGrid)
    for y in range(height):
        for x in range(width):
            print(printGrid[x][y], end='')
        print()

gridprint(grid)