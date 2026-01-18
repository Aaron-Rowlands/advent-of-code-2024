# class Map
## new Map(inputString)
### self.regions = self.parseInput(inputString)
## void parseInput
### self.regions = []
### coveredPlants = []
### for each cell in input:
#### if cell.value in coveredPlants continue
##### ⚠ doesn't work, the input contains multiple regions with the same plant ⚠
#### else
##### add to coveredPlants
##### self.parseShape(selfInput, inputString)
## int getFencingPrice
### return sum of region.getFencingPrice() for all self.regions

# class Region
## new Region(shape)
## int getFencingPrice
### return self.getArea * self.getPerimeter

# class Shape
## new Shape()
## moveCursor(direction in NESW)
