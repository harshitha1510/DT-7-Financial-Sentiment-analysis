from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method=="POST":
        msg=request.form.get()
        print(msg)
if __name__=="__main__":
    app.run()