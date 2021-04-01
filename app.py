import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')


def ValuePredictor(to_predict_list):
    test = to_predict_list
    print(test)
    # reshapping the input in the shape according to the featur columns
    to_predict = np.array(to_predict_list).reshape(1, 9)
    # importing the model and standard scaler from the pickel file

    std_scl = pickle.load(open("scaler_sel.pkl", "rb"))
    final_ar = std_scl.transform(to_predict)
    loaded_model = pickle.load(open("lr_reg.pkl", "rb"))
    result = loaded_model.predict_proba(final_ar)
    # print(loaded_model.predict_proba(final_ar))
    print(result)
    return result


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        print(result)
        success = result[0][1]
        print(success)
        # if int(result)==1:
        #     prediction='Success'
        # else:
        #     prediction='Fail'
        # logodds = loaded_model.intercept_[0]
        # odds = np.exp(logodds)
        # print(odds)
        # prob = odds / (1 + odds)
        # prob[0]+
        return render_template("result.html", prediction=success)


if __name__ == '__main__':
    # load_model()  # load model at the beginning once only
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
