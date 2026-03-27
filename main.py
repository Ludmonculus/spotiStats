import matplotlib.pyplot as plt
import pandas as pd


def pandaReader(filepath):    
    dataFrame = pd.read_json(filepath)
    return dataFrame

def plotter(frame):
    frame.plot()
    plt.savefig('dGraf.png')
    plt.show()



def main():
    df = pandaReader('streamingHistory.json')
    plotter(df)
    #print(df.to_string())

if __name__ == "__main__":
    main()