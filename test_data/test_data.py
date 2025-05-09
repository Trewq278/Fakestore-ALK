import csv

class DataReader:
    """
    Utility class for reading CSV test data files.
    """
    @staticmethod
    def get_csv_data(filename):
        """
        Reads a CSV file and returns a list of tuples containing card data.
        Args: filename (str): Path to the CSV file.
        Returns: list of tuples: Each tuple contains (description, card number, CVC, expiry date).
        """
        rows = []
        with open(filename, 'r') as data_file:
            reader = csv.reader(data_file)
            next(reader, None)  # Skip the header row
            for row in reader:
                rows.append((row[0], row[1], row[2], row[3]))  # description, number, CVC, date
        return rows