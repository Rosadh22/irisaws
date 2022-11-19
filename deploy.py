from flask import Flask,render_template, request
import pickle

app=Flask(__name__)

#load the model
with open("knn.pkl","rb") as f:
    load_model=pickle.load(f)

@app.route('/')
def home():
    result=" "
    return render_template('index.html',**locals())

@app.route('/predict',methods=['POST'])
def predict():
    sepal_length=float(request.form['sepal_length'])
    sepal_width=float(request.form['sepal_width'])
    petal_length=float(request.form['petal_length'])
    petal_width=float(request.form['petal_width'])

    result=load_model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    return render_template('index.html',**locals())

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)