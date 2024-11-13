from BLL.classes.BasicVisualizer import BasicVisualizer
import matplotlib.pyplot as plt

class MultiPlotVisualizer(BasicVisualizer):
    def plot_multiple(self):
        fig, axs = plt.subplots(2, 2, figsize=(12, 10))
        average_price_per_year = self.data.groupby('Year_of_Manufacture__c')['Sale_Price__c'].mean()
        axs[0, 0].plot(average_price_per_year.index, average_price_per_year.values, marker='o', linestyle='-')
        axs[0, 0].set_title('Sale Price Over Year')
        
        axs[0, 1].scatter(self.data['Mileage__c'], self.data['Sale_Price__c'])
        axs[0, 1].set_title('Milage vs Sale Price')

        self.data['Condition__c'].value_counts().plot(kind='bar', ax=axs[1, 0])
        axs[1, 0].set_title('Condition Distribution')

        self.data['Fuel_Type__c'].value_counts().plot(kind='pie', ax=axs[1, 1], autopct='%1.1f%%')
        axs[1, 1].set_title('Fuel Type Distribution')
        
        plt.tight_layout()
        plt.show()
