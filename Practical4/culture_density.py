# Start with the initial density
initial_density = 5
# Initialize the day counter
day = 1
# Initialize the current density
current_density = initial_density
# Use while Loop until the density exceeds 90%
while current_density <= 90:
    # Double the density each day
    current_density *= 2
    day += 1
# Calculate the number of days that required to exceed 90% density
holiday_days = day - 1
print(f"On day {holiday_days}, the cell density goes over 90%. This is the maximum number of days you can have a holiday from the lab.")