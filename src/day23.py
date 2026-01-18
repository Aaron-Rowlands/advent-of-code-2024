# main
#   collectAllConnections(input)
#   getGroupsOfThreeComputers(nodesWithConnections)
#   filterGroupsWithoutComputerT(groupsOfThree)
#   return filteredGroupsOfThree / 3 # groups of size three are counted three times

# collectAllConnections(pairConnections)
#   for pair in pairConnections
#     left, right = getMembers(pair) # create if missing
#     addConnection(left, right)

# addConnection(left, right)
#   left.addConnection(right)
#   right.addConnection(left)

# getGroupsOfThreeComputers(nodes)
#   for node in nodes:
#     if connectionCount >= 2:
#       for (node1, node2) in node.permutationsOfTwo():
#         resultList.add([node, node1, node2])

#   filterGroupsWithoutComputerT(groups)
#     for group in groups:
#       if group.find(key = it.startsWith('t'))
#         resultList.add(group)
#     return resultList
  
