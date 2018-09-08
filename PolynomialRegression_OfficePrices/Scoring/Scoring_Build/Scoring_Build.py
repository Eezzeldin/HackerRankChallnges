from Modeling_Dev import PolyPredict
import pandas as pd


def ModelScoring(ModelPrediction,True_Value):
    d = abs (True_Value - ModelPrediction) /10
    print ('d: ' ,d)
    print ('d-0.1: ' , d-0.1)
    d_adjusted = max (d-0.1,0)
    print ('d_adjusted: ', d_adjusted)
    print ('1-d_adjusted: ', 1-d_adjusted)
    Score = max (1-d_adjusted,0)
    print ('Score', Score)
    return float (Score)



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
    print ("=="*40)
    print ("Model Scores")
    ModelScores = [ModelScoring (Prediction,TrueValue) for Prediction,TrueValue in zip(Predictions_list,True_Values_list)]
    print (ModelScores)
