# Ytb-latest-Vids-Cron
An Api that can fetch the latest videos on Youtube for each 10 sec for a particular given keyword

Options:- This same stuff can be done using Node/ExpressJS and FASTAPI and Flask, I have opted for Flask due to short time available. (Finished off all stuff in two hours with API tesing and all other stuffs, got late due to some issues in getting the asynchronous manner of code as Python natively doesn't support asynchronous unless Async IO is used)

* Problem Statement / Tasks:- 

- [x] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

- [ ] It should be scalable and optimized 


Approach:- 

1. Generated the API key from Google console for Youtube Data v3
2. Used request/response in Python to fetch the data using `keyword` and `publishedAfter` and using 1 min lag for current datetime extracted the latest videos uploaded in this 1 min time and set a cron job for accessing it every 10s
3. Threaded the API so that it works asynchronously and the database can be accessed any time though the fetching process works behind the scenes
4. Discarded any repeated video fetched by checking the title and ensured no redundant data is present

* The api is somewhat optimized in the sense that it doesn't call redundant data and can't comment on scalability as the API can be made more faster if other DB is used than TinyDB but tinydb has access time very fast

How to run the code:- 

1. First put in the API key as a placeholder in the file `api_test.py`
2. Then run api_test.py as `python3 api_test.py`
3. Trigger the API using postman by sending a request in the form of JSON as:- `{"search_q":"cricket"}`
4. Then send a request to `127.0.0.1:800/vid_req` using POSTMAN

Eg:- 

![](https://github.com/dubesar/Ytb-latest-Vids-Cron/blob/main/picture.PNG?raw=true)

5. Now send another request with data field as none and to `127.0.0.1:800/qdb_req` and you will get all the data collected in the json form
6. The second request can be sent any time while the api is running.



