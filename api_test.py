# -*- coding: utf-8 -*-
from datetime import datetime, timezone                                
import os
import googleapiclient.discovery
from tinydb import TinyDB, Query
import flask
import time
import json


app = flask.Flask(__name__)
db = TinyDB('db.json')
Task = Query()

@app.route("/vid_req",methods=['GET', 'POST'])
def latestVideoYtb():
    query_req = flask.request.get_json(force=True)
    search_q = query_req["search_q"]

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "0"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "ENTER YOUR API KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    while(True):
        local_time = datetime.now(timezone.utc).astimezone()
        publishTime = local_time.isoformat()
        print(publishTime)
        time.sleep(60)
        request = youtube.search().list(
            part="snippet",
            maxResults=25,
            publishedAfter=publishTime,
            q='cricket'
        )
        response = request.execute()

        # print(response)

        for i in response['items']:
            new_snip = i['snippet']
            print(new_snip)
            if(db.search(Task.title != new_snip['title'])):
                db.insert({'time':new_snip['publishedAt'],'description':new_snip['description'],'title':new_snip['title'],'thumbnails':new_snip['thumbnails']})
        time.sleep(10)

    return response

@app.route("/qdb_req",methods=['GET', 'POST'])
def qDB():
    li = db.all()
    jsonStr = json.dumps(li)
    return jsonStr


if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 800,threaded=True)
