from flask import jsonify
from dao import TVKatalogueDao


class TVKatalogueHandler:
    def build_tvkatalogues_dict(self, row):
        result = {}
        result['TVKID'] = row[0]
        result['UID'] = row[1]
        result['TVID'] = row[2]
        result['TVKUStatus']=row[3]
        result['TVKUSeason']=row[4]
        result['TVKUEpisode']=row[5]
        return result
    #Unique ID
    #UserID
    #TVshow ID
    #TVKatalogue User Status (Watching, Planning to watch, etc)
    #TVKUSeason is self explanatoru (season count)
    #TVKUEpisode is self explanatory (episode count)
    #TVKUActivity is a deletion flag. Not sure if 0 is active or inactive. Decide with team later.
    
    def build_tvkatalogues_attributes(self, TVKID, UID, TVID, TVKUStatus, TVKUSeason, TVKUEpisode,):
        result = {}
        result['TVKID'] = TVKID
        result['UID'] = UID
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

    def getTVKatalogueById(self, json):
        TVKID=json["TVKID"]
        dao = TVKatalogueDao.TVKatalogueDAO()
        row = dao.getTVKatalogueById(TVKID)
        if not row:
            return jsonify(Error = "tvkatalogue Not Found"), 404
        else:
            tvkatalogues = self.build_tvkatalogues_dict(row)
            return jsonify(tvkatalogues = tvkatalogues)

    def getTVKatalogueByUId(self, json):
        uid = json["UID"]
        dao = TVKatalogueDao.TVKatalogueDAO()
        row = dao.getTVKatalogueByUID(uid)
        if not row:
            return jsonify(Error = "tvkatalogue Not Found"), 404
        else:
            tvkatalogues = self.build_tvkatalogues_dict(row)
            return jsonify(tvkatalogues = tvkatalogues)

    def insertTVKatalogueJson(self, json):
            uid = json['UID']
            tvid = json['TVID']
            tvkustatus=json['TVKUStatus']
            tvkuseason = json['TVKUSeason']
            tvkuepisode=json['TVKUEpisode']
            dao = TVKatalogueDao.TVKatalogueDAO()
            row = dao.getExistingEntry(uid, tvid)
            if row:
                return jsonify(Error = "Entry Exists."), 404
            else:
                if uid and tvid and tvkustatus and tvkuseason and tvkuepisode:
                    tvkid = dao.insert(uid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                    result = self.build_tvkatalogues_attributes(tvkid, uid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                    return jsonify(tvkatalogues=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteTVkatalogue(self, TVKID):
        dao = TVKatalogueDao.TVKatalogueDAO()
        if not dao.getTVKatalogueById(TVKID):
            return jsonify(Error = "tvkatalogue not found."), 404
        else:
            dao.delete(TVKID)
            return jsonify(DeleteStatus = "OK"), 200

    def updateTVkatalogueJson(self, json):
        dao = TVKatalogueDao.TVKatalogueDAO()
        tvkid = json['TVKID']
        uid = json['UID']
        tvid = json['TVID']
        tvkustatus = json['TVKUStatus']
        tvkuseason = json['TVKUSeason']
        tvkuepisode =json['TVKUEpisode']
        if not dao.getTVKatalogueById(tvkid):
            return jsonify(Error="TVWL not found."), 404
        else:
            if tvkid and uid and tvid and tvkustatus and tvkuseason and tvkuepisode:
                dao.update(tvkid, uid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                result = self.build_tvkatalogues_attributes(tvkid, uid, tvid, tvkustatus, tvkuseason, tvkuepisode)
                return jsonify(tvkatalogues=result), 200