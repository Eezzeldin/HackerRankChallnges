from Modeling_Dev import PolyPredict
import pandas as pd


def ModelScoring(ModelPrediction,True_Value):
    d = (True_Value - ModelPrediction) /10
    d_adjusted = max (d-0.1,0)
    Score = max (1-d_adjusted,0)
    return Score



if __name__ == "__main__":
    DataPath = '/Users/emadezzeldin/Dropbox/PhD/HackerRank/HackerRankChallnges/PolynomialRegression_OfficePrices/Modeling/Data/'
    NewData= pd.read_csv (DataPath+ 'TestData_Predictors.csv')
    Degree = 4
    Predictions_list = PolyPredict (NewData,Degree).tolist()
    print ("=="*40)
    print ("Poly Order " + str (Degree) + " Predictions")
    print (Predictions_list)
    True_Values = pd.read_csv (DataPath+'TestData_Responce.csv').values
    True_Values_list = [row[0] for row in True_Values.tolist()]
    print ("=="*40)
    print ("True Values")
    print (True_Values_list)
