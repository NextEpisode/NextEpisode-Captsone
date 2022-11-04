from flask import Flask, request
from handler.UserHandler import UserHandler
from handler.MovieKatalogueHandler import MovieKatalogueHandler
from handler.TVKatalogueHandler import TVKatalogueHandler
from flask_cors import CORS

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)


@app.route('/')
def greeting():
    return 'Welcome!!!'


##Request JSON Changes (For UID)
#Implement Get All (And test potential code issues)



#User Area ------------------------------------------------------
@app.route('/user', methods=['GET'])
def users():
    if request.method == 'GET':
            return UserHandler().getAllUsers()

@app.route('/user/opt', methods=['GET', 'POST', 'PUT'])
def useropt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return UserHandler().getUserByGoogleId(request.json)
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return UserHandler().insertUserJson(request.json)
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return UserHandler().updateUserJson(request.json)


#User Area ------------------------------------------------------

#Forum Area Begin

#Forum Area End

#Movie Area-----------------------------------------------------------------
#Segment of Code for Routes regarding Movie or TV katalogues

@app.route('/moviekatalogue', methods=['GET'])
def mk():
    if request.method == 'GET':
            return MovieKatalogueHandler().getAllMovieKatalogues()

@app.route('/moviekatalogue/opt', methods=['GET', 'POST', 'PUT'])
def mkopt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().getMovieKatalogueByUId(request.json)
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().insertMovieKatalogueJson(request.json)
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return MovieKatalogueHandler().updateMovieKatalogueJson(request.json)


#Movie Area-----------------------------------------------------------------
#TV Area--------------------------------------------------------------------

@app.route('/tvkatalogue', methods=['GET'])
def tv():
    if request.method == 'GET':
            return TVKatalogueHandler().getAllTVKatalogues()

@app.route('/tvkatalogue/opt', methods=['GET', 'POST', 'PUT'])
def tvopt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return TVKatalogueHandler().getTVKatalogueByUId(request.json)
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return TVKatalogueHandler().insertTVKatalogueJson(request.json)
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return TVKatalogueHandler().updateTVkatalogueJson(request.json)

#TV Area--------------------------------------------------------------------

if __name__ == '__main__':
    app.run()