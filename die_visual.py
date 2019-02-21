from die import Die
import pygal

# Creates 2 dice
die1 = Die()
die2 = Die()
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

    # Analyze results
    # Stores the number of times each value is rolled
    frequencies = []
    max_result = die1.num_sides + die2.num_sides
    # Count how many times each number appears in results
    for value in range(2, max_result+1):
        # Count how many times each numbers appears in the list
        frequency = results.count(value)

        # Adds the value to the list
        frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

# Title and axes of histogram
hist.title = "Rolling 2 dice results 1000x"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', 12]
hist.x_title = "Number of rolls"
hist.y_title = "Frequency of number on die"

# Adds data to histogram
hist.add('Six Sided Die', frequencies)

# Saves file
hist.render_to_file('die_visual.svg')
