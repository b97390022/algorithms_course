# Course1-Week2-Merge sort
import os


def sort_and_count(L):
    if len(L) == 1:
        return L, 0
    else:
        B, x = sort_and_count(L[: len(L) // 2])
        C, y = sort_and_count(L[len(L) // 2 :])
        D, z = merge_and_count_split(B, C)
        return D, x + y + z


def merge_and_count_split(B, C):
    D = list(range(len(B) + len(C)))
    count = 0
    i = 0
    j = 0
    for k in range(0, len(B) + len(C)):
        if i < len(B) and j < len(C):
            if B[i] < C[j]:
                D[k] = B[i]
                i += 1
            else:
                D[k] = C[j]
                j += 1
                count += len(B) - i

        elif i >= len(B):
            D[k] = C[j]
            j += 1
        else:
            D[k] = B[i]
            i += 1

    return D, count


if __name__ == "__main__":
    # file_path = r"/content/drive/MyDrive/week2_text.txt"
    file_path = os.path.abspath(os.getcwd()) + r"\txt files\Merge sort.txt"

    with open(
        file_path,
        mode="r",
    ) as f:
        text_lists = [int(i.replace("\n", "")) for i in f.readlines()]

    print(sort_and_count(text_lists))
