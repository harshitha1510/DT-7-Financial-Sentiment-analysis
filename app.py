from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
SAI-YASHWANTH
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST": 


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
main
        msg=request.form.get("message")
        print(msg)
    else:
        return render_template("predict.html")

 SAI-YASHWANTH
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5151)
=======
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050)
    main
