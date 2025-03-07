import numpy as np

lst = []
with open ('route.txt') as f:
    lst = f.read()

#print(lst[:50])

splited_lines = lst.split('\n')
#print(splited_lines[:5])

f_list = []
s_list = []
no_spaces =[]
for line in splited_lines:
    no_spaces = line.split()
    #print(no_spaces)
    f_list.append(int(no_spaces[0]))
    s_list.append(int(no_spaces[1]))
    

f_list = sorted(f_list)
s_list = sorted(s_list)
#print(f_list[:5], '\n',s_list[:5])


total_sum = 0
for i in range(len(f_list)):
    total_sum += abs(f_list[i] - s_list[i])

print(total_sum)

sim_score = 0
for nm in f_list:
    sim_score += nm * s_list.count(nm)

print(sim_score)