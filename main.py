import csv

# Define data
data = [
    (1, "A towel,", 1.0),
    (42, " it says, ", 2.0),
    (1337, "is about the most ", -1),
    (0, "massively аваывапывап useful thing ", 123),
    (-2, "an interstellar hitchрпарпаропhiker can have.", 3),
]

# Write CSV file
with open("test.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(data)