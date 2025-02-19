def foobar(lin, index):
    for i in range(1, index):
        prev = lin[i-1]
        curr = lin[i]
        if prev > curr:
            lin[i-1] = curr
            lin[i] = prev
    return lin

foobar([12, 6, 18], 2)


def foobar_sort(l_unsortiert):
    for i in range(len(l_unsortiert), 0, -1):
        l_unsortiert= foobar(l_unsortiert, i)
    return l_unsortiert

foobar_sort([1,4,5,4,3,78,9])


# Worst case: Liste ist in absteigender Reihenfolge sortiert, also [n, n-1, ..., 3, 2, 1]

# Laufzeit: O(n^2)
# Speicher: O(1)

