# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:10:25 2020

@author: Pradipkumar
"""

from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route("/")
def fun():
    return render_template("twitter.html")

@app.route("/predict",methods=["POST"])
def fun2():
    tweet=list(request.form["tweet"].split("\n"))
    pipeline=pickle.load(open("pipeline.pickle","rb"))
    val=pipeline.predict(tweet)
    return "predicted tweet is {}".format(val)

if __name__=="__main__":
    app.run(debug=True)