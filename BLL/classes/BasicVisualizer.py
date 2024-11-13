import matplotlib.pyplot as plt
import pandas as pd

class BasicVisualizer:
    def __init__(self, data):
        self.data = data

    # def plot_line_chart(self, x_column, y_column):
    #     plt.figure(figsize=(10, 5))
    #     plt.plot(self.data[x_column], self.data[y_column])
    #     plt.xlabel(x_column)
    #     plt.ylabel(y_column)
    #     plt.title(f"{y_column} over {x_column}")
    #     plt.show()

    def plot_line_chart(self, x_column, y_column):
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()

        # Побудова лінійного графіка
        plt.figure(figsize=(10, 6))
        plt.plot(average_price_per_year.index, average_price_per_year.values, marker='o', color='g', linestyle='-')
        #plt.title("Середня ціна автомобілів за роками виробництва")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.show()
