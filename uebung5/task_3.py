def create_buckets(numb):
    return [[] for _ in range(numb)]


def add_to_bucket(buckets, vals, n) :
    for val in vals:
        index = val % n
        buckets[index].append(val)
    return buckets




def good_bucket_count(unsorted):
    return max(1, len(unsorted) // 5)


def flatten(buckets):
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))
    return sorted_list


def radix_light(unsorted):
    n = good_bucket_count(unsorted)
    buckets = create_buckets(n)
    buckets = add_to_bucket(buckets, unsorted, n)
    return sorted(flatten(buckets))

test_list = [29, 10, 14, 37, 13, 23, 7, 5, 20, 31]
radix_light(test_list)