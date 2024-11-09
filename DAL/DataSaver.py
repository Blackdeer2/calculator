import json
import csv

class DataSaver:
    @staticmethod
    def save_as_json(data, filename):
        with open(f"{filename}.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def save_as_csv(data, filename):
        with open(f"{filename}.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())
            for row in data:
                writer.writerow(row.values())

    @staticmethod
    def save_as_txt(data, filename):
        with open(f"{filename}.txt", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
