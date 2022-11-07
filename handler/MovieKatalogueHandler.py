from flask import jsonify
from dao import MovieKatalogueDao


class MovieKatalogueHandler:
    def build_moviekatalogues_dict(self, row):
        result = {}
        result['MKID'] = row[0]
        result['UID'] = row[1]
        result['MovieID'] = row[2]
        result['MKUStatus']=row[3]
        return result

    def build_moviekatalogues_attributes(self, MKID, UID, MovieID, MVKUStatus):
        result = {}
        result['MKID'] = MKID
        result['UID'] = UID
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

    def getMovieKatalogueById(self, json):
        MKID = json["MKID"]
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        row = dao.getMovieKatalogueById(MKID)
        if not row:
            return jsonify(Error = "Katalogue Not Found"), 404
        else:
            moviekatalogues = self.build_moviekatalogues_dict(row)
            return jsonify(moviekatalogues = moviekatalogues)

    def getMovieKatalogueByUId(self, json):
        UID=json["UID"]
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        row = dao.getMovieKatalogueByUID(UID)
        if not row:
            return jsonify(Error = "Katalogue Not Found"), 404
        else:
            moviekatalogues = self.build_moviekatalogues_dict(row)
            return jsonify(moviekatalogues = moviekatalogues)

    def insertMovieKatalogueJson(self, json):
            uid = json['UID']
            movieid = json['MovieID']
            mkustatus = json['MKUStatus']
            dao = MovieKatalogueDao.MovieKatalogueDAO()
            row = dao.getExistingEntry(uid, movieid)
            if row:
                return jsonify(Error = "Entry Exists."), 404
            else:
                if uid and movieid and mkustatus:
                    mkid = dao.insert(uid, movieid, mkustatus)
                    result = self.build_moviekatalogues_attributes(mkid, uid, movieid, mkustatus)
                    return jsonify(moviekatalogues=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteMovieKatalogue(self, uid):
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        if not dao.getMovieKatalogueById(uid):
            return jsonify(Error = "Katalogue not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateMovieKatalogueJson(self, json):
        dao = MovieKatalogueDao.MovieKatalogueDAO()
        mkid = json['MKID']
        uid = json['UID']
        movieid = json['MovieID']
        mkustatus = json['MKUStatus']
        if not dao.getMovieKatalogueById(mkid):
            return jsonify(Error="Movie Katalogue not found."), 404
        else:
            if mkid and uid and movieid and mkustatus:
                dao.update(mkid, uid, movieid, mkustatus)
                result = self.build_moviekatalogues_attributes(mkid, uid, movieid, mkustatus)
                return jsonify(moviekatalogues=result), 200