import numpy as np
import matplotlib.pyplot as plt

def show_chart():

    # Creating dataset
    sentiment = ['NEGATIVE', 'NEUTRAL', 'POSITIVE','INVALID']
    
    data = [390, 367, 410,21]
    
    
    # Creating explode data
    explode = (0.0, 0.0, 0.0, 0.0)
    
    # Creating color parameters
    colors = ( "red", "grey", "green",'black')
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "black" }
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    explode = explode,
                                    labels = sentiment,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="black"))
    
    # Adding legend
    ax.legend(wedges, sentiment,
            title ="Sentiment Polarity",
            loc ="center left",
            bbox_to_anchor =(1.07, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 12, weight ="bold")
    ax.set_title("Without Emoji")
    
    plt.savefig('C:/Users/AlphaQuadrant/Documents/thesis-development/sentiment-analysis-thesis/Interface/static/images/chart.png') 

    # show plot
    plt.show()

    
show_chart()
