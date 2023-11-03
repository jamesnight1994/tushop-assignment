'''
1. Get the number of jobs to be done
2. Get the sort the jobs in ascending order 
3. IF the start time is greater than the end time of the previous job then take the job
4. IF the start time is lesser than the end time of the previous job 
5. THEN check the if profit of the overlapping job is greater than that of the previous job THEN make it the previous job instead

This will allow John to maximize his profits

'''
# read job details from the user
def read_jobs():
    n = int(input("Enter the number of Jobs\n"))
    jobs = []
    for _ in range(n):
        start_time = int(input("Enter job start time: "))
        end_time = int(input("Enter job end time: "))
        profit = int(input("Enter earnings: "))
        jobs.append((start_time, end_time, profit))
    return jobs

# calculate remaining jobs and earnings for other employees
def calculate_remaining_jobs(jobs):
    # Sort jobs based on end times ascending whcih is equal to start to the first key in the turple
    jobs.sort(key=lambda x: x[1])
    # remaining jobs will be equal to the number of jobs in the 
    remaining_jobs = len(jobs)
    # jobs taken by the john
    jobs_taken = []
    previous_job = (0000,0000,0)
    for job in jobs:
        start_time, end_time, profit = job
        previous_start_time, previous_end_time, previous_profit = previous_job
        job_taken = None
        # if the start_time of the job starts after that of the previous job taken
        if start_time >= previous_end_time:
            # take the job
            job_taken = job
            jobs_taken.append(job_taken)
        elif start_time < previous_end_time and profit > previous_profit:
            # remove the previous job ....
            jobs_taken.remove(previous_job)
            # ... and take this job instead
            job_taken = job
            jobs_taken.append(job_taken) 
        # then the previous job will be equal to the job taken before we move to the next
        previous_job = job_taken
    # total earning
    total_earnings = sum(profit for _, _, profit in jobs)
    # taken_earnings taken by john
    taken_earnings = sum(profit for _, _, profit in jobs_taken)
    # deduct the jobs taken by John from the total jobs
    remaining_jobs -= len(jobs_taken)
    # deduct the earnings taken by John from the total earning
    remaining_earnings = total_earnings - taken_earnings
    return remaining_jobs, remaining_earnings

# Main function to handle input and output
def main():
    jobs = read_jobs()
    remaining_jobs, remaining_earnings = calculate_remaining_jobs(jobs)
    print("The number of tasks and earnings available for others employees")
    print("Task:", remaining_jobs)
    print("Earnings remaining:", remaining_earnings)

# Run the main function
if __name__ == "__main__":
    main()
