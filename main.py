from flask import Flask, request
from flask import jsonify
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
            return UserHandler().getAllUsers() #Works

@app.route('/user/opt', methods=['GET', 'POST', 'PUT', 'DELETE'])
def useropt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return UserHandler().getUserByGoogleId(request.json) #Works
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return UserHandler().insertUserJson(request.json) #Works
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return UserHandler().updateUserJson(request.json)#Works
            else:
                 if request.method == "DELETE":
                    print("REQUEST: ", request.json)
                    return UserHandler().deleteUser(request.json)

#User Area ------------------------------------------------------

                 
#Movie Area-----------------------------------------------------------------
#Segment of Code for Routes regarding Movie or TV katalogues

@app.route('/moviekatalogue', methods=['GET'])
def mk():
    if request.method == 'GET':
            return MovieKatalogueHandler().getAllMovieKatalogues() #Works


@app.route('/moviekatalogue/opt', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mkopt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().getAllMovieKataloguesByKID(request.json) #Works
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().insertMovieKatalogueJson(request.json) #Works
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return MovieKatalogueHandler().updateMovieKatalogueJson(request.json) #Works
            else:
                 if request.method == "DELETE":
                    print("REQUEST: ", request.json)
                    return MovieKatalogueHandler().deleteMovieKatalogue(request.json) #Works
                 
#Search by Status. Try to put this with the rest later.
@app.route('/moviekatalogue/stat', methods=['GET'])
def mkstat():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().getAllMovieKataloguesByStatus(request.json) #Works
#Movie Area-----------------------------------------------------------------
#TV Area--------------------------------------------------------------------

@app.route('/tvkatalogue', methods=['GET'])
def tv():
    if request.method == 'GET':
            return TVKatalogueHandler().getAllTVKatalogues() #Works

@app.route('/tvkatalogue/opt', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tvopt():
    if request.method == 'GET':
            print("REQUEST: ", request.json)
            return TVKatalogueHandler().getAllTVKataloguesByKID(request.json)#Works
    else:
        if request.method == 'POST':
            print("REQUEST: ", request.json)
            return TVKatalogueHandler().insertTVKatalogueJson(request.json)#Works
        else:
            if request.method == "PUT":
                print("REQUEST: ", request.json)
                return TVKatalogueHandler().updateTVkatalogueJson(request.json)#Works
            else:
                 if request.method == "DELETE":
                    print("REQUEST: ", request.json)
                    return TVKatalogueHandler().deleteTVkatalogue(request.json) #Works
                 
    #Works. Put with the rest later.
@app.route('/tvkatalogue/stat', methods=['GET'])
def tvkstat():
    if request.method == 'GET':
        print("REQUEST: ", request.json)
        return TVKatalogueHandler().getAllTVKataloguesByStatus(request.json)#Works

#TV Area--------------------------------------------------------------------
#Purge Area--------------------------------------------------------------------
#Working on it
@app.route('/purge', methods=['DELETE'])
def purge():
    print("REQUEST: ", request.json)
    uid = request.json("UID")
    gid = request.json("GID")
    if uid and gid:
        UserHandler().deleteUser(request.json)
        TVKatalogueHandler().deleteTVkatalogue(request.json)
        MovieKatalogueHandler().deleteMovieKatalogue(request.json)
        return jsonify(DeleteStatus = "Purge Complete."), 200
    else:
         return jsonify(Error="Information Incorrect."), 404
    

#KID Purge
@app.route('/moviekatalogue/prg', methods=['DELETE'])
def mkprg():
    if request.method == 'DELETE':
            print("REQUEST: ", request.json)
            return MovieKatalogueHandler().deleteAllMovieKataloguesByKID(request.json) #Works
    
#KID Purge
@app.route('/tvkatalogue/prg', methods=['DELETE'])
def tvkprg():
    if request.method == 'DELETE':
            print("REQUEST: ", request.json)
            return TVKatalogueHandler().deleteAllTVKataloguesByKID(request.json) #Works


    #Maybe Method
# Purge Area--------------------------------------------------------------------

#Singular Updates (TV)#Nice to have, in progress)
#Filter by status (Katalogues)#Done.
#Change the Database to what we decided. KID to UID and removed TVKID and MVKID. #Done May have to add Email to User tomorrow.
#Purge delete, (Done) and multi-delete.(Nice to have, in progress.)




if __name__ == '__main__':
    app.run()