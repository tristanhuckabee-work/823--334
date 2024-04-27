# Recall the merge sort algorithm:
    
# 1. Find midpoint to divide list in half
# 2. Call `merge_sort` recursively on the first half
# 3. Call `merge_sort` recursively on the second half
# 4. Merge the two sorted halves with `merge`

# Implement the `merge_sort` function with the `merge` helper function.

# Write your code here.
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst

#     mid = len(lst) // 2
#     first_half = merge_sort(lst[:mid])
#     second_half= merge_sort(lst[mid:])
    
#     return merge(first_half, second_half)



# def merge(first_half, second_half):
#     i = j = 0
#     res = []

#     while i < len(first_half) or j < len(second_half):
#         if i == len(first_half):
#             res.append(second_half[j])
#             j += 1
#         elif j == len(second_half):
#             res.append(first_half[i])
#             i += 1
#         elif first_half[i] > second_half[j]:
#             res.append(second_half[j])
#             j += 1
#         else:
#             res.append(first_half[i])
#             i += 1
#     return res

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

lst = [5, 2, 38, 91, 16, 427]

sorted_lst = merge_sort(lst)        # Out of place solution
print(sorted_lst)

merge_sort(lst)                     # In place solution
print(lst)