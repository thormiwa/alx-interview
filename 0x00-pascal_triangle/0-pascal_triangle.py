def pascal_triangle(n):
   trow = []
   for x in range(1, n+1):
       row = []
       for a in range(x):
           if a == 0 or a == x-1:
               n = 1
               row.append(n)
           else:
                n = trow[x-2][a-1] + trow[x-2][a]
                row.append(n)
       trow.append(row)

   return trow
