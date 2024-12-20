from flask import Flask, render_template, request
import pandas as pd
from src.pipeline.Prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        if request.method == 'GET':
            return render_template('prediction.html')
        else:
            data = CustomData(
                battery_power=request.form.get("battery_power"),
                blue=request.form.get("blue"),
                clock_speed=request.form.get("clock_speed"),
                dual_sim=request.form.get("dual_sim"),
                fc=request.form.get("fc"),
                four_g=request.form.get("four_g"),
                int_memory=request.form.get("int_memory"),
                m_dep=request.form.get("m_dep"),
                mobile_wt=request.form.get("mobile_wt"),
                n_cores=request.form.get("n_cores"),
                pc=request.form.get("pc"),
                px_height=request.form.get("px_height"),
                px_width=request.form.get("px_width"),
                ram=request.form.get("ram"),
                sc_h=request.form.get("sc_h"),
                sc_w=request.form.get("sc_w"),
                talk_time=request.form.get("talk_time"),
                three_g=request.form.get("three_g"),
                touch_screen=request.form.get("touch_screen"),
                wifi=request.form.get("wifi")
            )
            df = data.get_data_as_dataframe()
            pipeline = PredictPipeline()
            prediction = pipeline.predict(df)
            if prediction == 1:
                price_range = "Low"
            elif prediction == 2:
                price_range = "Medium"
            elif prediction == 3:
                price_range = "High"
            return render_template('prediction.html', price_range=price_range)

    except Exception as e:
        return render_template("prediction.html",price_range=f"An error occured: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)