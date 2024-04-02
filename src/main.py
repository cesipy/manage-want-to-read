import csv
import pandas as pd
import os

def markdown_to_csv(md_file, csv_file):
    with open(md_file, "r") as md, open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for line in md:
            if line.startswith('- [ ]'):
                text = line.replace('- [ ] ', '').strip()
                writer.writerow([text])
            elif line.startswith('- [x]'):
                text = line.replace('- [x] ', '').strip()
                writer.writerow([text])


def clear_file(file_path):
    open(file_path, 'w').close()


def main():
    path_md  = "../res/want-to-read-old.txt"
    path_goodreads_csv = "../res/goodreads_library_export.csv"
    path_csv_md = "../res/temp.txt"

    clear_file(path_csv_md)
    markdown_to_csv(path_md, path_csv_md)

    df1 = pd.read_csv(path_goodreads_csv, usecols=['Title'])
    df2 = pd.read_csv(path_csv_md, usecols=['Title'])

    merged_df = pd.concat([df1, df2])

    merged_df.drop_duplicates(inplace=True)

    merged_df.to_csv('../out/merged.csv', index=False)
    os.remove(path_csv_md)

    


if __name__ == '__main__':
    main()
