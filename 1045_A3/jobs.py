def max_sales(street):


    if len(street) == 0:
        return 0

    else:
        sales = 0

        if street[1] < street[2]:
            sales += street[0]
            i = 2

        else:
            sales += street[1]
            i = 3

        while i < len(street) - 1:
            if (street[i-1] < street[i]) and (street[i+1] < street[i]):   # i think i need to change this one.
                sales += street[i]
                i += 2
            else:
                i += 1

        if street[-1] > street[i-1]:
            sales += street[-1]

    # after the loop's finished, check the amount.
    return sales


def is_burger(breads):

    opening = []
    closing = []
    output = []

    # intial check is to see if the amount of opening breads == closing breads.
    for i in range(len(breads)):
        if breads[i][0] == 'o':
            opening.append(breads[i])
        else:
            closing.append(breads[i])

    if len(opening) != len(closing):
        return False

    else:
        while len(breads) > 0:
            temp = breads.pop()
            compare1 = temp

            if len(output) == 0:
                output.append(temp)
            else:
                compare2 = output.pop()
                # the follow checks whether the bread is opening or closing AND whether the types of bread match, hence, [-1]
                if (compare1[0] == 'o' and compare2[0] == 'c') and (compare1[-1] == compare2[-1]):
                        pass
                else:
                    output.append(compare2)
                    output.append(compare1)

        # this checks if there's any other values that need to be checked.
        if len(output) == 0:
            return True
        else:
            return False


















