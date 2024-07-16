import pandas as pd
import matplotlib.pyplot as plt


#WHEN FINISH THE GAME UNINSTALL PANDAS AND MATPLOTLIB  

def put_hist_in_csv(hist):
    df = pd.DataFrame(list(hist.items()), columns=['BOX', 'Amount of hits'])
    df.to_csv('betting_data_analisys/1000bets_16layers.csv')
    
    
def generate_hist():
    df = pd.read_csv('betting_data_analisys/1000bets_16layers.csv')
    
    keys = df['BOX']
    values = df['Amount of hits']
    
    plt.figure(figsize=(10, 5))
    plt.bar(keys, values, color='skyblue')
    plt.xlabel('boxes')
    plt.ylabel('amount of balls')
    plt.title('Histogram of betting results')
    plt.show()
    
    