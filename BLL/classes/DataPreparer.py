class DataPreparer:
    def __init__(self, data):
        self.data = data

    def prepare_data_for_visualization(self):
        # Example: Drop rows with missing data
        self.data.dropna(inplace=True)
        # Additional transformations can go here
        return self.data
