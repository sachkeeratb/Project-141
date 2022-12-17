from flask import Flask,jsonify,request
import csv
import pandas as pd

df1 = pd.read_csv('./articles.csv')

headerList = ['id', 'index', 'timestamp', 'eventType', 'contentId', 'authorPersonId', 'authorSessionId', 'authorUserAgent', 
'authorRegion', 'authorCountry', 'contentType', 'url', 'title', 'text', 'lang', 'total_events']

# Uneccesary because it is completed
# df.to_csv("articles.csv", header=headerList, index=False)

df1.to_csv("all_articles.csv", header=False, index=False)

all_articles = []
liked_articles = []
not_liked_articles = []

app = Flask(__name__)

with open('all_articles.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

@app.route("/get-article")
def get_movie():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
        })

@app.route("/liked-articles",methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "success"
    }), 201

@app.route("/unliked-not_liked_articles",methods=["POST"])
def liked_movie():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status" : "success"
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=9090)
