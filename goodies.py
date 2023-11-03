'''
1. Read input data from the sample_input.txt file, including the number of employees and the list of goodies with their respective prices.
2. Store the goodies and prices in a dictionary data structure.
3. Sort the goodies in ascending order based on their prices.
4. Iterate through the sorted goodies list to find the consecutive subsets of goodies equal to the number of employees.
5. Calculate the price difference between the first and last goodies in each subset.
6.Track the subset with the minimum price difference.
7. Write the selected goodies and their prices, along with the calculated price difference, to the sample_output.txt file.
'''
# Read input from sample_input.txt
with open('sample_input.txt', 'r') as file:
    lines = file.readlines()

# Extract number of employees
num_employees = int(lines[0].split(': ')[1])
#  Extract goodies with prices
goodies = {}
for line in lines[2:]:
    name, price = line.strip().split(': ')
    goodies[name] = int(price)

# Sort goodies by price in ascending order
sorted_goodies = sorted(goodies.items(), key=lambda x: x[1])

# Find minimum difference
min_diff = float('inf')
selected_goodies = []
for i in range(len(sorted_goodies) - num_employees + 1):
    diff = sorted_goodies[i + num_employees - 1][1] - sorted_goodies[i][1]
    if diff < min_diff:
        min_diff = diff
        selected_goodies = sorted_goodies[i:i + num_employees]

# Write output to sample_output.txt
with open('sample_output.txt', 'w') as file:
    file.write('The goodies selected for distribution are:\n')
    for goodie, price in selected_goodies:
        file.write(f'{goodie}: {price}\n')
    file.write(f'And the difference between the chosen goodie with highest price and the lowest price is {min_diff}')
