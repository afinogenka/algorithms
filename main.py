# create array from user input

rows = int(input('enter number of rows:'))
columns = int(input('enter number of columns:'))
arr = []

for i in range(rows):
    inner_arr = []
    for j in range(columns):
        value = int(input())
        inner_arr.append(value)
    arr.append(inner_arr)
print(arr)

# selection sort
for i in range(rows):
    for j in range(columns):
        for k in range(rows):
            for l in range(columns):
                if arr[i][j] < arr[k][l]:
                    temp = arr[i][j]
                    arr[i][j] = arr[k][l]
                    arr[k][l] = temp
print(arr)



