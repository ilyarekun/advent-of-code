'''


....xxmas.
.samxmS...
...S..a...
..A.A.Ms.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX



horisontal xmas
horisontal samx

vertical x
         m
         a
         s
         
vertical s
         a
         m
         x
         
diagonal 
x
 m 
  a
   s
   
diagonal 
s
 a 
  m
   x
   
diagonal 
   x
  m 
 a
s 

diagonal 
   s
  a 
 m
x            
'''


import numpy as np

#print(np.ones([3,3]))
def part_1(path):
   with open(path, 'r') as f:
      lines = f.read().split()
      
   #print(len(lines), ' : len lines \n', type(lines), ' : type lines \n', all([len(el) == len(lines[0]) for el in lines]))


   count_xmas = 0
   count_samx = 0
   for el in lines:
      count_xmas += el.count('XMAS')
      count_samx += el.count('SAMX')

   #print(f"in lines xmas: {count_xmas}")
   #print(f"in lines samx: {count_samx}")

   arr_lines = []
   for i in range(0,len(lines)):
      arr_lines.append(list(lines[i]))

   #print(arr_lines[:5])
   #print(''.join([arr_lines[0][0],arr_lines[1][0],arr_lines[2][0],arr_lines[3][0]]))

   count_horiz_xmas = 0 
   count_horiz_samx = 0
   count_vert_xmas = 0 
   count_vert_samx = 0

   count_dig_main_xmas = 0
   count_dig_main_samx = 0
   count_dig_comain_xmas = 0
   count_dig_comain_samx = 0

   row_len = len(arr_lines[0])
   col_len = len(arr_lines)

   for i in range(0, col_len):
      for j in range(0, row_len):
         # horisontal xmas
         if(j < row_len - 3 and ''.join(arr_lines[i][j:j+4]) == 'XMAS'):
            count_horiz_xmas += 1
         # horisontal samx
         if(j < row_len - 3 and ''.join(arr_lines[i][j:j+4]) == 'SAMX'):
            count_horiz_samx += 1
         # vertical xmas
         if(i < col_len - 3 and ''.join([arr_lines[i][j],arr_lines[i+1][j],arr_lines[i+2][j],arr_lines[i+3][j]]) == 'XMAS'):
            count_vert_xmas += 1
         # vertical samx
         if(i < col_len - 3 and ''.join([arr_lines[i][j],arr_lines[i+1][j],arr_lines[i+2][j],arr_lines[i+3][j]]) == 'SAMX'):
            count_vert_samx += 1
            
            
            
         # diagonal main xmas
         if(j < row_len - 3 and i <col_len - 3 and ''.join([arr_lines[i][j],arr_lines[i+1][j+1],arr_lines[i+2][j+2],arr_lines[i+3][j+3]]) == 'XMAS'):
            count_dig_main_xmas +=1
         # diagonal main samx
         if(j < row_len - 3 and i <col_len - 3 and ''.join([arr_lines[i][j],arr_lines[i+1][j+1],arr_lines[i+2][j+2],arr_lines[i+3][j+3]]) == 'SAMX'):
            count_dig_main_samx +=1
            
         # diagonal comain xmas
         if(j < row_len - 3 and i >= 3 and ''.join([arr_lines[i][j],arr_lines[i-1][j+1],arr_lines[i-2][j+2],arr_lines[i-3][j+3]]) == 'XMAS'):
            count_dig_comain_xmas +=1
         # diagonal comain samx
         if(j < row_len - 3 and i >= 3 and ''.join([arr_lines[i][j],arr_lines[i-1][j+1],arr_lines[i-2][j+2],arr_lines[i-3][j+3]]) == 'SAMX'):
            count_dig_comain_samx +=1
         

   print(count_horiz_xmas + count_horiz_samx + count_vert_xmas+ count_vert_samx+ count_dig_main_xmas+ count_dig_main_samx+ count_dig_comain_xmas+ count_dig_comain_samx )


def part_2(path):
   with open(path, 'r') as f:
      lines = f.read().split()
      
      arr_lines = []
   for i in range(0,len(lines)):
      arr_lines.append(list(lines[i]))


   row_len = len(arr_lines[0])
   col_len = len(arr_lines)
   
   pattern_count = 0
   
   for i in range(col_len-2):
      for j in range(row_len-2):
         if arr_lines[i][j] == 'M' == arr_lines[i+2][j] and arr_lines[i][j+2] == 'S' == arr_lines[i+2][j+2] and arr_lines[i+1][j+1] == 'A':
            pattern_count += 1
         if arr_lines[i][j] == 'S' == arr_lines[i+2][j] and arr_lines[i][j+2] == 'M' == arr_lines[i+2][j+2] and arr_lines[i+1][j+1] == 'A':
            pattern_count += 1
            
         if arr_lines[i][j] == 'M' == arr_lines[i][j+2] and arr_lines[i+2][j] == 'S' == arr_lines[i+2][j+2] and arr_lines[i+1][j+1] == 'A':
            pattern_count += 1   
         if arr_lines[i][j] == 'S' == arr_lines[i][j+2] and arr_lines[i+2][j] == 'M' == arr_lines[i+2][j+2] and arr_lines[i+1][j+1] == 'A':
            pattern_count += 1  
   return pattern_count



if __name__=='__main__':
   #part_1('xmas.txt')
   print(part_2('xmas.txt'))
   
   
   

   """
   
   
1
   
m.s
.a.
m.s

2
s.m
.a.
s.m

3
m.m
.a.
s.s

4
s.s
.a.
m.m
   """