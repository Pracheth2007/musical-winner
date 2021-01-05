import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open("cups of coffee vs hours of sleep.csv") as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="sleep in hours", y="Coffee in ml")
        fig.show()

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open("cups of coffee vs hours of sleep.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Coffee in ml"]))
            days_present.append(float(row["sleep in hours"]))

    return {"x" : marks_in_percentage, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
