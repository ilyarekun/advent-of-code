

with open("rows.txt", "r") as f:
    data = f.read().split('\n')

#print(data[:3])
for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])
        

def safe_check(rep):
    if all([rep[i] > rep[i+1] for i in range(len(rep)-1)]) or all([rep[i] < rep[i+1] for i in range(len(rep)-1)]):
        if all([1<=abs(rep[i] - rep[i+1])<=3 for i in range(len(rep)-1)]):
            return True
    return False


num_safe = 0

for rep in data:
    if safe_check(rep):
        num_safe += 1
    else:
        for i in range(len(rep)):
            line = rep[:]
            del line[i]
            if safe_check(line):
                num_safe += 1
                break


print(num_safe)









        