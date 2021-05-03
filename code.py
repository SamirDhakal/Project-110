import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

population_st = statistics.stdev(data)
print(population_mean, population_st)

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    
    fig = ff.create_distplot([df], ['mean'], show_hist = False)
    fig.show()
    
def setup():
    mean_list = []
    for i in range(0,100):
        setofmeans = randomsetofmean(30)
        mean_list.append(setofmeans)
    show_fig(mean_list)
    
setup()