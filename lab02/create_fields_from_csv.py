import csv


def main():
    # get headers
    with open("../lab01/data/matches_serie-a.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        data = [row for row in reader]

    # headers to fields.txt
    with open("fields.txt", "w") as txt_file:
        for header in headers[1:]:
            txt_file.write("".join(header) + "\n")

    # rest of the data without headers
    with open("matches_serie-a_without_headers.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


if __name__ == "__main__":
    main()
