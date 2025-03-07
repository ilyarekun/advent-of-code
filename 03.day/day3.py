"""
x mul(2,4) %&mul[3,7]!@^do_not_ mul(5,5) +mul(32,64]then( mul(11,8) mul(8,5) )
"""

from string import Template as tmp
import re
from operator import itemgetter

with open("mul_data.txt", 'r') as f:
    data = f.read()



pattern_mul = "(mul[(]\d+[,]\d+[)])"
pattern_do = "(do[(][)])"
pattern_dont = "(don't[(][)])"
#right = re.findall(pattern,data)

#for a in right[:20]:
#    print(a)

matches_mul = re.finditer(pattern_mul, data)
matches_do = re.finditer(pattern_do, data)
matches_dont = re.finditer(pattern_dont, data)

#print(match.start())
lst_mul, lst_do, lst_dont = [], [], []
for match_mul in matches_mul:
    mul_o = match_mul.group()
    num1, num2 = map(int,re.findall('\d+',mul_o))
    lst_mul.append([num1,num2, match_mul.start()])

#print(lst_mul[:10], '\n', len(lst_mul))

for match_do in matches_do:
    lst_do.append([0, 'do', match_do.start()])


for match_dont in matches_dont:
    lst_dont.append([0, 'dont', match_dont.start()])

main_lst = lst_do + lst_dont + lst_mul

s = sorted(main_lst, key = itemgetter(2))
#for el in s:
#    print(el)
sum_s = 0
mode = 'on'

for i in range(len(s)):
    if s[i][1] == 'do':
        mode = 'on'
    if s[i][1] == 'dont':
        mode = 'off'
    if type(s[i][1]) is int and mode == 'on':
        sum_s += s[i][0]*s[i][1]
    print(s[i], mode)

    
print(sum_s)




"""

x mul(2,4) &mul[3,7]!^ don't ()_ mul(5,5) +mul(32,64]( mul(11,8) un do() ? mul(8,5) )

"""