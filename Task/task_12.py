# Pattern

# for r in range(1,6):
#     i = 64
#     for c in range(r):
#         print(chr(i+r),end=" ")
#     print(" ")

for r in range(1,6):
    for c in range(r):
        print(chr(65+c),end=" ")
    print(" ")
