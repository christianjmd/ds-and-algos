"""
popular function: returns a list of people who at least n friends.
    - each person is identified by the number of their vertex.
    - examples:
        a) Calling popular(clayton list,2) returns [0,1,2,3].
        b) Calling popular(clayton list,3) returns [0].
        c) Calling popular(clayton list,0) returns [0,1,2,3,4].
"""

def popular(graph_list, n):

    output = []

    for i in range(len(graph_list)):
        if len(graph_list[i]) >= n:
            output.append(i)

    return output

"""
friend of a friend function: determines whether two people have exactly one degree
                                of separation. whether two people aren't friends
                                but at least one friend in common

    - examples: clayton_matrix = [ [0,1,1,1,0],
[1,0,0,1,0],
[1,0,0,0,1],
[1,1,0,0,0],
[0,0,1,0,0] ]
    - a) Calling foaf(clayton matrix,0,4) returns True as 0 and 4 are both friends with 2.
      b) Calling foaf(clayton matrix,0,3) returns False as 0 and 3 are friends directly.
      c) Calling foaf(clayton matrix,1,4) returns False as 1 and 4 have no friends in common.

"""

def foaf(graph_matrix, person1, person2):

    counter = 0

    if (graph_matrix[person1][person2] == 0) and (graph_matrix[person2][person1] == 0):

        for j in range(len(graph_matrix)):
            if graph_matrix[person1][j] and graph_matrix[person2][j] == 1:
                counter = counter + 1

    if counter >= 1:
        return True
    else:
        return False

"""
society function: determines whether a person has two friends who are also friends
                  with each other.

Input: a nested list graph matrix that represents a graph as an adjacency matrix, that models the friendships
at Monash; and an integer person, where 0  person < number of people on campus.
Output: a boolean,

examples:
a) Calling society(clayton matrix,0) returns True as 1 and 3 are both friends with 0.
b) Calling society(clayton


"""
def society(graph_matrix, person):

    friends = []
    counter = 0

    for i in range(len(graph_matrix)):
        if graph_matrix[person][i] == 1:
            friends.append(i)

    if len(friends) == 2:
        if graph_matrix[friends[0]][friends[1]] and graph_matrix[friends[1]][friends[0]] == 1:
            counter = counter + 1

    if len(friends) > 2:
        if graph_matrix[friends[0]][friends[1]] and graph_matrix[friends[1]][friends[0]] == 1:
            counter = counter + 1
        if graph_matrix[friends[0]][friends[2]] and graph_matrix[friends[2]][friends[0]] == 1:
            counter = counter + 1
        if graph_matrix[friends[1]][friends[2]] and graph_matrix[friends[2]][friends[1]] == 1:
            counter = counter + 1

    if counter >= 1:
        return True
    else:
        return False
