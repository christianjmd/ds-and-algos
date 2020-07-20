def ternary(lst):

    pivot = lst[0]
    swap_pos = 1
    output = []

    for i in range(1, len(lst) - 1):
        # if it belongs on the left
        if (lst[i] < pivot):
            lst[i], lst[swap_pos] = lst[swap_pos], lst[i]
            swap_pos += 1

    # bring pivot to correct position.
    lst[0], lst[swap_pos-1] = lst[swap_pos-1], lst[0]
    output.append(swap_pos - 1)     # final position of the integer.

    for j in range(swap_pos, len(lst)):
        if lst[j] == pivot:
            lst[j], lst[swap_pos] = lst[swap_pos], lst[j]
            swap_pos += 1
    output.append(swap_pos)     # swap_pos increased by one before it got swapped.

    return output
