# n^2 solution
# def h_index(A):
#     index = 0
#     prev_index = 0
#     while True:
#         curr_papers = 0
#         for i in A:
#             if i >= index:
#                 curr_papers += 1
#         if curr_papers < index:
#             return prev_index
#         else:
#             prev_index = index
#         index += 1

# divide and conquer
def h_index(A):
    middle = len(A) // 2
    h_index = len(A) - middle
    
    while h_index < A[middle]:
        middle += 1
        h_index += 1
    while h_index > A[middle]:
        middle -= 1
        h_index -= 1
    return h_index

print(h_index([6,5,3,1,0]))