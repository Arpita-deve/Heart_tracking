from flask import Flask,render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('heart.html')
@app.route("/print")
def action():
    with open('GNB.pkl','rb') as f:
        gnb=pickle.load(f)
    age = request.args.get("age")
    sex = request.args.get("sex")
    cp = request.args.get("cp")
    trtbps= request.args.get("trtbps")
    chol = request.args.get("chol")
    fbs= request.args.get("fbs")
    restecg = request.args.get("restecg")
    thalachh = request.args.get("thalachh")
    exng = request.args.get("exng")
    oldpeak = request.args.get("oldpeak")
    slp = request.args.get("slp")
    caa = request.args.get("caa")
    thall = request.args.get("thall")

    l=[float(age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall)]
    pred=gnb.predict(l)
    prob=gnb.predict_proba(1)[:,1]

    return str(pred)+str(prob)
app.run(debug=True)
