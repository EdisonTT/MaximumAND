# Here a default list (array) is created. 
lis = [8,27,4,11,29]

#Finding the largest number, number of bits and the largest posible number.

max_num = max(lis)
max_num_bin_len = len(str(bin(max_num))) - 2
max_pos_num = 2**max_num_bin_len - 1
temp =[]
count = 0
ind = 0

#The very next two for loop will create the Matrix.

for num in lis:
    temp.append(list(map(int,list(str(bin(num))[2:]))))
for x in temp:
    for i in range(max_num_bin_len):
        if len(x)!=max_num_bin_len:
            x.insert(0,0)

#Inspecting the matrix.
#If a column with one zero exist, the variable count is set to 1.

for i in range(max_num_bin_len):
    for x in temp:
        if x[i]==0:
            count += 1
            ind_a = ind
        ind +=1
        if count==2:
            break        
    if count == 1:
        break
    count = 0
    ind = 0


result = max_pos_num

#If there exist a column with exactly one zero, code inside if statement is executed.

if count == 1:
    lis.pop(ind_a)
    lis.append(max_pos_num)
    for num in lis:
         result = result & num
    print(result)
else:
    for num in lis:
        result = result & num
        if result == 0:
            break
    print(result)     
