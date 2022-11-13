from flask import jsonify
from dao import TVKatalogueDao


class TVKatalogueHandler:
    def build_tvkatalogues_dict(self, row):
        result = {}
        result['KID'] = row[0]
        result['TVID'] = row[1]
        result['TVKUStatus']=row[2]
        result['TVKUSeason']=row[3]
        result['TVKUEpisode']=row[4]
        return result
    #Unique ID
    #UserID
    #TVshow ID
    #TVKatalogue User Status (Watching, Planning to watch, etc)
    #TVKUSeason is self explanatoru (season count)
    #TVKUEpisode is self explanatory (episode count)
    #TVKUActivity is a deletion flag. Not sure if 0 is active or inactive. Decide with team later.
    
    def build_tvkatalogues_attributes(self, KID, TVID, TVKUStatus, TVKUSeason, TVKUEpisode,):
        result = {}
        result['KID'] = KID
        result['TVID'] = TVID
        result['TVKUStatus']=TVKUStatus
        result['TVKUSeason']=TVKUSeason
        result['TVKUEpisode']=TVKUEpisode
        return result

    def getAllTVKatalogues(self):
        dao = TVKatalogueDao.TVKatalogueDAO()
        tvkatalogues_list = dao.getAllTVKatalogues()
        result_list = []
        for row in tvkatalogues_list:
            result = self.build_tvkatalogues_dict(row)
            result_list.append(result)
        return jsonify(tvkatalogues=result_list)
    
    def getAllTVKataloguesByKID(self, json):
        kid = json["KID"]
        dao = TVKatalogueDao.TVKatalogueDAO()
        tvkatalogues_list = dao.getTVKataloguesByKID(kid)
        result_list = []
        for row in tvkatalogues_list:
            result = self.build_tvkatalogues_dict(row)
            result_list.append(result)
        return jsonify(tvkatalogues=result_list)

    def getAllTVKataloguesByStatus(self, json):
        kid = json["KID"]
        status = json["TVKUStatus"]
        dao = TVKatalogueDao.TVKatalogueDAO()
        row = dao.getAllTVKataloguesByStatus(kid, status)
        if not row:
            return jsonify(Error = "Katalogues Not Found"), 404
        else:
            result_list = []
            for row in row:
                result = self.build_tvkatalogues_dict(row)
                result_list.append(result)
            return jsonify(tvkatalogues=result_list)

    def insertTVKatalogueJson(self, json):
            kid = json['KID']
            tvid = json['TVID']
            tvkustatus=json['TVKUStatus']
            tvkuseason = json['TVKUSeason']
            tvkuepisode=json['TVKUEpisode']
            dao = TVKatalogueDao.TVKatalogueDAO()
            row = dao.getExistingEntry(kid, tvid)
            if row:
                return jsonify(Error = "Entry Exists."), 404
            else:
                if kid and tvid and tvkustatus and tvkuseason and tvkuepisode:
                    dao.insert(kid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                    result = self.build_tvkatalogues_attributes(kid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                    return jsonify(tvkatalogues=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def updateTVkatalogueJson(self, json):
        dao = TVKatalogueDao.TVKatalogueDAO()
        kid = json['KID']
        tvid = json['TVID']
        tvkustatus = json['TVKUStatus']
        tvkuseason = json['TVKUSeason']
        tvkuepisode =json['TVKUEpisode']
        if not dao.getExistingEntry(kid, tvid):
            return jsonify(Error="Katalogue not found."), 404
        else:
            if kid and tvid and tvkustatus and tvkuseason and tvkuepisode:
                dao.updateKatalogue(kid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                result = self.build_tvkatalogues_attributes(kid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                return jsonify(tvkatalogues=result), 200
            
    #Delete multiple entries at once.
            
    def deleteTVkatalogue(self, json):
        dao = TVKatalogueDao.TVKatalogueDAO()
        kid = json['KID']
        tvid = json['TVID']
        if not dao.getTVKataloguesByKIDTVID(kid, tvid):
            return jsonify(Error = "tvkatalogue not found."), 404
        else:
            dao.delete(kid, tvid)
            return jsonify(DeleteStatus = "OK"), 200
        

    #Katalogue Purge.
    def deleteAllTVKataloguesByKID(self, json):
        dao = TVKatalogueDao.TVKatalogueDAO()
        kid = json['KID']
        dao.deleteAll(kid)
        return jsonify(DeleteStatus = "OK"), 200