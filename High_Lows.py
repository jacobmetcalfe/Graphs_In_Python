# Demonstration on how to download data sets from online sources
# 2 Common formats for this are CSV and JSON
# This plot will measure variations in weather data
# CSV Format = 2014-1-5,61,44,26,18,7,-1,56,30,20.9.... etc
# In this we will graph Colorado Springs Data from the past week
# Excel reader
import csv
# Graphing
from matplotlib import pyplot as plt
# To get the dates of the graph
from datetime import datetime
# Gets the first time of the day

# defines filename
filename = 'KCOCOLOR775_2019-02-13_2019-02-19.csv'

# Opens file and stores the object in f
with open(filename) as f:
    # Reads file and stores it in the reader
    reader = csv.reader(f)

    # Gets the next line, which is all of the headers
    header_row = next(reader)

    # Goes through the CSV file
    dates, temperatures = [], []
    for row in reader:
        # Gets the date of the date of the recorded temperature
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        # Casts each temp in row to an int
        temperature = float(row[2])
        # Adds each temp to the array temperature
        temperatures.append(temperature)

    # enumerates each column header and index
    for index, column_header in enumerate(header_row):
        print(index, column_header)


    # Plotting the actual data of temperatures in Colorado Springs
    # figure size
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # Plots the arrays in blue
    plt.plot(dates, temperatures, c='blue')

    # title of the graph
    plt.title("Temperatures in Colorado Springs, February 2018", fontsize=24)
    fig.autofmt_xdate()
    # Y Axis label
    plt.ylabel('Temperatures(F)', fontsize=16)
    # Which axis to have ticks, what axis major or minor, size of ticks
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Shows the plot
    plt.show()


    # Tip: Headers are not always labeled the same, should not be an issue but sometimes you are going to get extra
    # spaces, etc.
