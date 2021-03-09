import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from training import NoT,Sentiment 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'Sentiment': Sentiment,
         'Number of Tweets': NoT
        }
df1 = DataFrame(data1,columns=['Sentiment','Number of Tweets'])



root= tk.Tk() 
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Sentiment','Number of Tweets']].groupby('Sentiment').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('SENTIMENT ANALYSIS ON TWITTER')
root.mainloop()