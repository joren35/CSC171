import random
from collections import deque
import itertools
from heapq import heappush, heappop, heapify


class State:

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

class State2:

    def __init__(self, state2, parent2, move2, depth2, cost2, key2):

        self.state2 = state2

        self.parent2 = parent2

        self.move2 = move2

        self.depth2 = depth2

        self.cost2 = cost2

        self.key2 = key2

        if self.state2:
            self.map2 = ''.join(str(e) for e in self.state2)

    def __eq__(self, other):
        return self.map2 == other.map2

    def __lt__(self, other):
        return self.map2 < other.map2


goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_node = State
goal_node2 = State2
initial_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
board_len = 9
board_side = int(board_len ** 0.5)
given = list()
nodes_expanded = 0
max_search_depth = 0
max_frontier_size = 0
moves = list()
costs = set()


def bfs(start_state):
    global max_frontier_size, goal_node, max_search_depth
    explored, queue = set(), deque([State(start_state, None, None, 0, 0, 0)])
    while queue:

        node = queue.popleft()
        explored.add(node.map)
        if node.state == goal_state:
            goal_node = node
            return queue, len(explored)

        neighbors = expand(node)

        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > max_search_depth:
                    max_search_depth += 1

        if len(queue) > max_frontier_size:
            max_frontier_size = len(queue)

			
def astar_state(start_state):

    global max_frontier_size, goal_node2, max_search_depth
    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()
    key2 = h(start_state)
    root = State2(start_state, None, None, 0, 0, key2)
    entry = (key2, 0, root)
    heappush(heap, entry)
    heap_entry[root.map2] = entry

    while heap:

        node = heappop(heap)
        explored.add(node[2].map2)
        if node[2].state2 == goal_state:
            goal_node2 = node[2]
            print str(len(explored))+": Size2"
            return heap, len(explored)

        neighbors2 = expand2(node[2])

        for neighbor in neighbors2:
            neighbor.key2 = neighbor.cost2 + h(neighbor.state2)
            entry = (neighbor.key2, neighbor.move2, neighbor)
            if neighbor.map2 not in explored:
                heappush(heap, entry)
                explored.add(neighbor.map2)
                heap_entry[neighbor.map2] = entry

                if neighbor.depth2 > max_search_depth:
                    max_search_depth += 1

            elif neighbor.map2 in heap_entry and neighbor.key2 < heap_entry[neighbor.map2][2].key2:
                hindex = heap.index((heap_entry[neighbor.map2][2].key2,
                                     heap_entry[neighbor.map2][2].move2,
                                     heap_entry[neighbor.map2][2]))
                heap[int(hindex)] = entry
                heap_entry[neighbor.map2] = entry
                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)
			
			
def expand(node):
    global nodes_expanded
    nodes_expanded += 1
    neighbors = list()
    neighbors.append(State(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes = [neighbor for neighbor in neighbors if neighbor.state]
    return nodes
	
def expand2(node):
    global nodes_expanded
    nodes_expanded += 1
    neighbors2 = list()
    neighbors2.append(State2(move(node.state2, 1), node, 1, node.depth2 + 1, node.cost2 + 1, 0))
    neighbors2.append(State2(move(node.state2, 2), node, 2, node.depth2 + 1, node.cost2 + 1, 0))
    neighbors2.append(State2(move(node.state2, 3), node, 3, node.depth2 + 1, node.cost2 + 1, 0))
    neighbors2.append(State2(move(node.state2, 4), node, 4, node.depth2 + 1, node.cost2 + 1, 0))
    nodes2 = [neighbor for neighbor in neighbors2 if neighbor.state2]
    return nodes2

	
def move(state, position):
    new_state = state[:]
    index = new_state.index(0)

    if position == 1:  # Up
        if index not in range(0, board_side):

            temp = new_state[index - board_side]
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down
        if index not in range(board_len - board_side, board_len):

            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left
        if index not in range(0, board_len, board_side):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right
        if index not in range(board_side - 1, board_len, board_side):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None


def h(state):
    return sum(abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
               for b, g in ((state.index(i), goal_state.index(i)) for i in range(1, board_len)))


def backtrace():
    moves = []
    current_node = goal_node

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'up'
        elif current_node.move == 2:
            movement = 'down'
        elif current_node.move == 3:
            movement = 'left'
        else:
            movement = 'right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves
	

def backtrace2():
    moves = []
    current_node = goal_node2

    while initial_state != current_node.state2:

        if current_node.move2 == 1:
            movement = 'up'
        elif current_node.move2 == 2:
            movement = 'down'
        elif current_node.move2 == 3:
            movement = 'left'
        else:
            movement = 'right'

        moves.insert(0, movement)
        current_node = current_node.parent2

    return moves

	
def export(frontier):
    global moves
    moves = backtrace()
    print ("Shortest Path to Goal: " + str(moves))


def shuffler():
    given = goal_state[:]
    print ("Goal State:"+str(given))
    randommoves = randomshuffler()
    given = performpath(randommoves,given,0,'no')
    print (given)

    for i in range(0,9):
         if given[i] == 0:
            num = i
            print(num)
	
    for i in range(0,9):
        initial_state[i] = given[i]
        print(initial_state[i])

		
def performpath(moves,given,num,counter):
    shortestmove = moves[:]
    tempList = given[:]

    for element in shortestmove:
        if element == 'right':
            num = moveRight(tempList,num)
            if counter == 'yes':
                printer(tempList)
            

        elif element == 'left':
            num = moveLeft(tempList,num)
            if counter == 'yes':
                printer(tempList)
       

        elif element == 'up':
            num = moveUp(tempList,num)
            if counter == 'yes':
                printer(tempList)
          

        elif element == 'down':
            num = moveDown(tempList,num)
            if counter == 'yes':
                printer(tempList)

    return tempList
            
			
def moveDown(temp, num):
    temp[num] = temp[num+3]
    temp[num+3] = 0
    num = num + 3
    return num 

def moveRight(temp, num):
    temp[num] = temp[num+1]
    temp[num+1] = 0
    num = num + 1
    return num 

def moveUp(temp, num):
    temp[num] = temp[num-3]
    temp[num-3] = 0
    num = num - 3
    return num 

def moveLeft(temp, num):
    temp[num] = temp[num-1]
    temp[num-1] = 0
    num = num -1 
    return num 

	
def printer(solution):
    print (str(solution[0])+" "+str(solution[1])+" "+str(solution[2]))
    print (str(solution[3])+" "+str(solution[4])+" "+str(solution[5]))
    print (str(solution[6])+" "+str(solution[7])+" "+str(solution[8]))
    print ("\n")

	
def randomshuffler():
    randmoves = ['+1','-1','+3','-3']
    randpos = list()
    randnum = random.randint(20,70)
    check = 0
    
    for i in range(0,randnum):
        el = random.choice(randmoves)
        check = check + int(el)
        if check >= 0 and check <= 8:
            if int(el) == 1:
                randpos.append('right')
            elif int(el) == -1:
                randpos.append('left')
            elif int(el) == 3:
                randpos.append('down')
            elif int(el) == -3:
                randpos.append('up')

        else:
            check = check + (-1*int(el))

    return randpos