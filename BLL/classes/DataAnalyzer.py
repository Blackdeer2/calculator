class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_extreme_values(self):
        return self.data.describe().loc[['min', 'max']]
