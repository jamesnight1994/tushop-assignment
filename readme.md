# Problem 1 Solution

1. Get the number of jobs to be done
2. Get the sort the jobs in ascending order
3. IF the start time is greater than the end time of the previous job then take the job
4. IF the start time is lesser than the end time of the previous job
5. THEN check the if profit of the overlapping job is greater than that of the previous job THEN make it the previous job instead

This will allow John to maximize his profits

👇🏾👇🏾

Run `python factory.py`

![](factory.mp4)

# Problem 2 Solution

1. Read input data from the sample_input.txt file, including the number of employees and the list of goodies with their respective prices.
2. Store the goodies and prices in a dictionary data structure.
3. Sort the goodies in ascending order based on their prices.
4. Iterate through the sorted goodies list to find the consecutive subsets of goodies equal to the number of employees.
5. Calculate the price difference between the first and last goodies in each subset.
6. Track the subset with the minimum price difference.
7. Write the selected goodies and their prices, along with the calculated price difference, to the sample_output.txt file.

👇🏾👇🏾

Run `python goodies.py`

![](goodies.mp4)
