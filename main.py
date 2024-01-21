import timeit
import random
from typing import List, Tuple

def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def compare_sorting_algorithms(arr: List[int]) -> Tuple[float, float, float]:
    start_time = timeit.default_timer()
    insertion_sort(arr.copy())
    insertion_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    merge_sort(arr.copy())
    merge_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted(arr.copy())  # Python's built-in sort uses Timsort
    timsort_time = timeit.default_timer() - start_time

    return insertion_time, merge_time, timsort_time

insertion_times = []
merge_times = []
timsort_times = []

for _ in range(100):
    times = compare_sorting_algorithms([random.randint(0, 1000) for _ in range(1000)])
    insertion_times.append(times[0])
    merge_times.append(times[1])
    timsort_times.append(times[2])

print(f"Average insertion sort time: {sum(insertion_times) / len(insertion_times)}")
print(f"Average merge sort time: {sum(merge_times) / len(merge_times)}")
print(f"Average Timsort time: {sum(timsort_times) / len(timsort_times)}")