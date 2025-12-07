import csv

with open("../data/MachineLearningRating_v3.txt", "r", encoding="utf-8") as infile, \
     open("../data/MachineLearningRating_v3.csv", "w", newline="", encoding="utf-8") as outfile:

    reader = csv.reader(infile, delimiter='|')
    writer = csv.writer(outfile)

    for row in reader:
        writer.writerow(row)

print("Conversion complete!")
