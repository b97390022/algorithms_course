# Course1-Week3-Quick sort
import os
import random


def ChoosePivot(A, l, r, choose):
    if choose == "First":
        p = l
    elif choose == "Last":
        p = r
    elif choose == "Median":
        p = InsertionSort({A[l]: l, A[(l + r) // 2]: (l + r) // 2, A[r]: r})

    elif choose == "Random":
        p = random.randint(l, r)
    A[l], A[p] = A[p], A[l]
    return A


def InsertionSort(A):
    A_keys = [i for i in A.keys()]
    for i in range(len(A_keys)):
        key = A_keys[i]
        j = i - 1
        while key < A_keys[j] and j >= 0:
            A_keys[j + 1] = A_keys[j]
            j -= 1
        A_keys[j + 1] = key
    return A[A_keys[1]] if len(A) == 3 else A[A_keys[1]]


def QuickSort(A, l, r, c=0, choose="Median"):
    if len(A) <= 1:
        return A

    if l < r:
        c += r - l
        A = ChoosePivot(A, l, r, choose)
        i = l + 1
        for j in range(l + 1, r + 1):
            if A[j] < A[l]:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[l], A[i - 1] = A[i - 1], A[l]

        c = QuickSort(A, l, i - 2, c, choose)
        c = QuickSort(A, i, r, c, choose)

    return c


if __name__ == "__main__":

    # file_path = r'/content/drive/MyDrive/QuickSort.txt' test

    file_path = os.path.abspath(os.getcwd()) + r"\txt files\QuickSort.txt"

    with open(
        file_path,
        mode="r",
    ) as f:
        num_lists_1 = [int(i.replace("\n", "")) for i in f.readlines()]
        num_lists_2, num_lists_3, num_lists_4 = (
            num_lists_1.copy(),
            num_lists_1.copy(),
            num_lists_1.copy(),
        )

    a = QuickSort(num_lists_1, 0, len(num_lists_1) - 1, c=0, choose="First")
    b = QuickSort(num_lists_2, 0, len(num_lists_2) - 1, c=0, choose="Last")
    c = QuickSort(num_lists_3, 0, len(num_lists_3) - 1, c=0, choose="Median")
    d = QuickSort(num_lists_4, 0, len(num_lists_4) - 1, c=0, choose="Random")

    final = a, b, c, d

    print(final)
