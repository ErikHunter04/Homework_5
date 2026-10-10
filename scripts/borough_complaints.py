import argparse
import os.path
import csv
from datetime import datetime

from collections import Counter

module_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(module_path,"..","data")
CREATION_DATE_INDEX = 1
COMPLAINT_TYPE_INDEX = 5
BOROUGH_INDEX = 25

DATE_FMT = "%m/%d/%Y"

def format_date(date):
    return datetime.strptime(date, DATE_FMT)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_csv',required=True)
    parser.add_argument('-s','--start_date',required=True)
    parser.add_argument('-e','--end_date',required=True)
    parser.add_argument('-o','--output_file')

    args = parser.parse_args()
    input = os.path.join(data_path, args.input_csv)
    start = format_date(args.start_date)
    end = format_date(args.end_date)

    counts = get_counts(input, start, end)

    if args.output_file:
        output = os.path.join(data_path, args.output_file)
        with open(output, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["complaint type", "borough", "count"])
            for complaint, by_borough in counts.items():
                for borough, n in by_borough.items():
                    writer.writerow([complaint, borough, n])
    else:
        print_counts(counts)

def get_counts(input, start, end):
    counts = {}
    with open(input, "r", newline="") as f:
        for row in csv.reader(f):
            date = datetime.strptime(row[CREATION_DATE_INDEX][:10], DATE_FMT)
            complaint = row[COMPLAINT_TYPE_INDEX].title()
            borough = row[BOROUGH_INDEX].title()

            if date < start or date > end:
                continue
            if complaint not in counts:
                counts[complaint] = {}
            if borough not in counts[complaint]:
                counts[complaint][borough] = 0
            counts[complaint][borough] +=1
    return counts

def print_counts(dic):
    print("complaint type, borough, count")
    for complaint, by_borough in dic.items():
        for borough, count in by_borough.items():
            print(f"{complaint}, {borough}, {count}")

if __name__ == "__main__":
    main()
