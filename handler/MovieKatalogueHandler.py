from flask import jsonify
from dao import MovieKatalogueDao


class MovieKatalogueHandler:
    def build_moviekatalogues_dict(self, row):
        result = {}
        result['KID'] = row[0]
        result['MovieID'] = row[1]
        result['MKUStatus']=row[2]
        return result

    def build_moviekatalogues_attributes(self, KID, MovieID, MVKUStatus):
        result = {}
        result['KID'] = KID
        result['MovieID'] = MovieID
        result['MKUStatus']=MVKUStatus
        return result

    def getAllMovieKatalogues(self):
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        moviekatalogues_list = dao.getAllMovieKatalogues()
        result_list = []
        for row in moviekatalogues_list:
            result = self.build_moviekatalogues_dict(row)
            result_list.append(result)
        return jsonify(moviekatalogues=result_list)
    
    def getAllMovieKataloguesByKID(self, json):
        kid = json["KID"]
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        moviekatalogues_list = dao.getMovieKataloguesByKID(kid)
        result_list = []
        for row in moviekatalogues_list:
            result = self.build_moviekatalogues_dict(row)
            result_list.append(result)
        return jsonify(moviekatalogues=result_list)

    def getAllMovieKataloguesByStatus(self, json):
        kid = json["KID"]
        status = json["MKUStatus"]
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        row = dao.getMovieKataloguesByStatus(kid, status)
        if not row:
            return jsonify(Error = "Katalogues Not Found"), 404
        else:
            result_list = []
            for row in row:
                result = self.build_moviekatalogues_dict(row)
                result_list.append(result)
            return jsonify(moviekatalogues=result_list)

    def insertMovieKatalogueJson(self, json):
            kid = json['KID']
            movieid = json['MovieID']
            mkustatus = json['MKUStatus']
            dao = MovieKatalogueDao.MovieKatalogueDAO()
            row = dao.getExistingEntry(kid, movieid)
            if row:
                return jsonify(Error = "Entry Exists."), 404
            else:
                if kid and movieid and mkustatus:
                    dao.insert(kid, movieid, mkustatus)
                    result = self.build_moviekatalogues_attributes(kid, movieid, mkustatus)
                    return jsonify(moviekatalogues=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def updateMovieKatalogueJson(self, json):
        kid = json['KID']
        movieid = json['MovieID']
        mkustatus = json['MKUStatus']
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        if not dao.getExistingEntry(kid, movieid):
            return jsonify(Error="Movie Katalogue not found."), 404
        else:
            if kid and movieid and mkustatus:
                dao.update(kid, movieid, mkustatus)
                result = self.build_moviekatalogues_attributes(kid, movieid, mkustatus)
                return jsonify(moviekatalogues=result), 200
    
    def deleteMovieKatalogue(self, json):
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        kid = json['KID']
        movieid = json['MovieID']
        if not dao.getExistingEntry(kid, movieid):
            return jsonify(Error = "Katalogue not found."), 404
        else:
            dao.delete(kid, movieid)
            return jsonify(DeleteStatus = "OK"), 200
    
    #User Katalogue Purge.
    def deleteAllMovieKataloguesByKID(self, json):
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        kid = json['KID']
        dao.deleteAll(kid)
        return jsonify(DeleteStatus = "OK"), 200