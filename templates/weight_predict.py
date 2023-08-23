import pickle

defprediction(height):
    model=pickle.load(open('model1.pkl','rb'))
    weight=model.predict(height)
    print(weight)
    return weight