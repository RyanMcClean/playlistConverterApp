from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
urlList = []

def get_meme():
    #Uncomment these two lines and comment out the other url line if you want to use a specific meme subreddit
    # sr = "/elfie_cutie"
    # url = "https://meme-api.herokuapp.com/gimme" + sr
    url = "https://meme-api.herokuapp.com/gimme"
    urlList = []
    while True:
        response = json.loads(requests.request("GET", url).text)
        meme_large = response["url"]
        subreddit = response["subreddit"]
        if meme_large not in urlList:
            urlList.append(meme_large)
            return meme_large, subreddit
        print("searching for another image")
        print(len(urlList))
        if len(urlList) > 400:
            urlList = []
        # if meme_large.endswith(".gif"):
        #     return meme_large, subreddit
        # print("searching")


@app.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host='0.0.0.0', port=80)