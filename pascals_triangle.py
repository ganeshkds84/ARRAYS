def pascal_triangle(rows):
    triangle=[]
    prev=[]
    for i in range(rows):
        prev=[1]*(i+1)
        for j in range(1,i):
            prev[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(prev)
            
                
    return triangle
            
a=int(input("Enter no. of rows:"))               
print(pascal_triangle(a))
