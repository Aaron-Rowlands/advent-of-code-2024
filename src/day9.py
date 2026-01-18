# read input file into a string
## strip the end

# convert the disk map string into a memory object instance
## has method getChecksum and compress

# init: create the internal array
## if the string has an odd number of digits, just add a zero at the end for zero more empty spaces
### allows taking steps of two through the characters when interpreting them:
### file content instances, empty space, ...

# compress: swap EmptySpace and FileContent objects until compressed
## can detect isCompressed by comparing first empty index and last full index
### those are useful in swapping as well

# checksum: simple calculation over the entire memory bar
## just go through the index range, skip empty cells and add content ID * index for file content

