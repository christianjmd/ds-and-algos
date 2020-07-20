import math

# =========    TASK 1

def post_time(graph, path):
    output = 0

    for i in range(len(path) - 1):
        output += graph[path[i]][path[i + 1]]

    print(output)


# ==========    TASK 2

def min_extension(con, graph):  # ref. lecture 10, slide 34 + 35.

    min_weight = math.inf
    i = con[-1]

    for j in range(len(graph)):
        if (j not in con) and (0 < graph[i][j] < min_weight):
            v, w = i, j
            min_weight = graph[i][j]

    return v, w

def post_route(graph):          # ref. lecture 10, slide 34 + 35.

    con = [0]

    while len(con) < len(graph):
        i, j = min_extension(con, graph)
        con += [j]


    if len(con) == len(graph):
        con.append(0)
    print(con)

# ==========    TASK 3

def minimum_extension(conn, graph):  # ref. lecture 10, slide 34 + 35.

    min_weight = math.inf
    x = conn[-1]     # checks most recently added vertex.

    for y in range(len(graph)):
        if (y not in conn) and (0 < graph[x][y] < min_weight):
            a, b = x, y
            min_weight = graph[x][y]

    return a, b

def on_time(graph, days):          # ref. lecture 10, slide 34 + 35.

    path_outcomes = []          # list to check total of every minimum path outcome from [0,1], [0,2], [0,3] and [0.4]

    for u in range(1, len(graph)):  # this is checking every path outcome possible starting at 0.

        conn = [0]
        conn.append(u)
        added = 0
        added += graph[conn[-1]][0]


        while len(conn) < len(graph):    # loop to check min_weight of each path.
            x, y = minimum_extension(conn, graph)
            conn += [y]
            added += graph[x][y]

        if len(conn) == len(graph):
            added += graph[conn[-1]][0]

        path_outcomes.append(added)


    # after each path and it's total has been taken, check if it matches criteria.
    for l in range(len(path_outcomes)):

        if path_outcomes[l] <= days:
            return True

        else:
            return False



















