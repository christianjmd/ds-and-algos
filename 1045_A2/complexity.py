def local_peak(lst):

    high = len(lst) - 1           # ref. lecture 15, slides 18 - 22
    mid = (0 + high) // 2


    while (lst[mid] < lst[mid - 1]) or (lst[mid] < lst[mid + 1]):

        if lst[mid - 1] > lst[mid]:
            mid = mid - 1
        else:
            mid = mid + 1

    if lst[mid] > (lst[mid - 1] and lst[mid - 1]):
        print(mid)
    else:
        return None














