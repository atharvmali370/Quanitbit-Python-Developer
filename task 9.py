import statistics

# Define the dataset
data = [1, 2, 2, 3, 4]

# Calculate mean
mean = statistics.mean(data)

# Calculate median
median = statistics.median(data)

# Calculate mode
mode = statistics.mode(data)

# Print the results
print("mean : {0}".format(mean))
print("median : {0}".format(median))
print("mode : {0}".format(mode))