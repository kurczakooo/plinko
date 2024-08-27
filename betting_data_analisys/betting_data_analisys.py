import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#WHEN FINISH THE GAME UNINSTALL PANDAS AND MATPLOTLIB  

def put_hist_in_csv(hist):
    df = pd.DataFrame(list(hist.items()), columns=['BOX', 'Amount of hits'])
    df.to_csv('betting_data_analisys/1000bets_16layers.csv')
    
    
def generate_hist():
    df = pd.read_csv('betting_data_analisys/1000bets_16layers.csv')
    
    #sns.set_style(style='darkgrid')
    
    plt.figure(figsize=(10, 5))
    
    sns.barplot(x='BOX', y='Amount of hits', data=df, palette='viridis')
    plt.title('Histogram of betting results')
    plt.show()
    
    