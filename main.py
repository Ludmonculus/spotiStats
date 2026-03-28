import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#import math

#hämta spotifydata, visa statistik på:
    #mest spelade artist 
    #mest spelade låt 


def panda_reader(filepath):    
    data_frame = pd.read_json(filepath)
    data_frame['minutes'] = (data_frame["msPlayed"]/(1000*60)).round(1)
    return data_frame

def plotter(d_frame, plotname, filename, xName, yName):
    #d_frame.plot()
    plt.figure(figsize=(20, 6))
    plt.savefig('graf.png')
    sns.barplot(data=d_frame.head(10), x=xName, y=yName, color= 'green') 
    
    plt.title(plotname)
    plt.savefig(filename)
    #plt.show()

#total lyssningstid per artist
def df_sum(d_frame):
            
    return d_frame.groupby('artistName')['minutes'].sum().reset_index()
    

#mest lyssnade låt
def df_max(d_frame):
    # .reset_index() gör om resultatet från en Series till en DataFrame
    return d_frame.groupby('trackName')['minutes'].sum().sort_values(ascending=False).reset_index()




def main():
    df = panda_reader('streamingHistory.json')
    #plotter(df)

    max_df= df_max(df)
     # Gör bilden lite bredare
    plotter(max_df, "mest spelade låt", "top_songs.png", "trackName", "minutes")
    print(max_df.to_string())

    sum_df = df_sum(df)
    plotter(sum_df, "total speltid per artist", "ms_played.png", "artistName", "minutes")

    print(sum_df.to_string())

if __name__ == "__main__":
    main()