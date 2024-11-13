from BLL.classes.AdvancedVisualizer import AdvancedVisualizer
from BLL.classes.BasicVisualizer import BasicVisualizer
from BLL.classes.DataAnalyzer import DataAnalyzer
from BLL.classes.DataPreparer import DataPreparer
from BLL.classes.MultiPlotVisualizer import MultiPlotVisualizer
from DAL.DataLoader import DataLoader

def main():
    filepath = "C:/VOVA/5 semester/SMP/calculator/Source/CarsCSV.csv"
    loader = DataLoader(filepath)
    data = loader.get_data()
    
    analyzer = DataAnalyzer(data)
    print(analyzer.get_extreme_values())
    
    preparer = DataPreparer(data)
    prepared_data = preparer.prepare_data_for_visualization()
    
    basic_vis = BasicVisualizer(prepared_data)
    basic_vis.plot_line_chart('Mileage__c', 'Sale_Price__c')
    
    adv_vis = AdvancedVisualizer(prepared_data)
    adv_vis.plot_scatter('Mileage__c', 'Sale_Price__c')
    adv_vis.plot_bar_chart('Engine_Power__c', 'Sale_Price__c')
    
    multi_vis = MultiPlotVisualizer(prepared_data)
    multi_vis.plot_multiple()



if __name__ == "__main__":
    main()