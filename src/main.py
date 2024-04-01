import csv
import pandas as pd

def markdown_to_csv(md_file, csv_file):
    with open(md_file, "r") as md, open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for line in md:
            if line.startswith('- [ ]'):
                text = line.replace('- [ ]', '')
                writer.writerow([text])


def main():
    path = "../res/goodreads_library_export.csv"
    df1 = pd.read_csv(path, usecols=['Title'])

    print(df1)


main()
