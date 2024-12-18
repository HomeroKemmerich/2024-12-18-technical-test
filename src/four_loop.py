# Make a loop from 1 to 100. If the number is a multiple of 4, calculate elevate
# to the square. Else, elevate to the cube. The end result should be a 
# dictionary where the key is the original number, and the value is the 
# calculated number. Print the result.

results = {}

for i in range(1, 100):
    if i % 4 == 0:
        results[f'{i}'] = pow(i, 2)
    else:
        results[f'{i}'] = pow(i, 3)

print(results)