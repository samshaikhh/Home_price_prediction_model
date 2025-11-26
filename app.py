from flask import Flask,request,render_template,url_for,redirect
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("Home_price_prd_model.pkl")

@app.route('/',methods=['GET','POST'])
def house():
    predict_price = None

    if request.method=='POST':
        area = float(request.form['area'])
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        location_rating = float(request.form['location_rating'])
        age = float(request.form['age'])

        data = np.array([[area,bedrooms,bathrooms,location_rating,age]])

        predict_price = round(model.predict(data)[0],2)
        
    return render_template('home.html',predict_price=predict_price)


if __name__ == "__main__":
    app.run(debug=True)