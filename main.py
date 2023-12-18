import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
        return header, data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return None, None

def display_csv(header, data):
    if header and data:
        print(','.join(header))
        for row in data:
            print(','.join(row))
    else:
        print("Unable to display CSV.")

def find_min_max(data):
    if data:
        values = [int(value) for row in data for value in row[1:]]
        min_value = min(values)
        max_value = max(values)
        return min_value, max_value
    else:
        return None, None

def write_results_to_csv(min_value, max_value):
    try:
        with open('results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Min Value', 'Max Value'])
            writer.writerow([min_value, max_value])
        print("Results written to 'results.csv'")
    except Exception as e:
        print(f"Error writing results to file: {e}")

if __name__ == "__main__":
    input_file_path = "data.csv"

    header, data = read_csv(input_file_path)
    display_csv(header, data)

    min_value, max_value = find_min_max(data)

    if min_value is not None and max_value is not None:
        write_results_to_csv(min_value, max_value)
