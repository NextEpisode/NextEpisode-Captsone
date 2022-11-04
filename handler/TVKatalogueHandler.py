from flask import jsonify
from dao import TVKatalogueDao


class TVKatalogueHandler:
    def build_tvkatalogues_dict(self, row):
        result = {}
        result['TVKID'] = row[0]
        result['UID'] = row[1]
        result['TVID'] = row[2]
        result['TVKUStatus']=row[3]
        return result

    def build_tvkatalogues_attributes(self, TVKID, UID, TVID, TVKUStatus):
        result = {}
        result['TVKID'] = TVKID
        result['UID'] = UID
        result['TVID'] = TVID
        result['TVKUStatus']=TVKUStatus
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
            if uid and tvid and tvkustatus:
                dao = TVKatalogueDao.TVKatalogueDAO()
                TVKID = dao.insert(uid, tvid, tvkustatus)
                result = self.build_tvkatalogues_attributes(TVKID, uid, tvid, tvkustatus)
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
        if not dao.getTVKatalogueById(tvkid):
            return jsonify(Error="TVWL not found."), 404
        else:
            if tvkid and uid and tvid and tvkustatus:
                dao.update(tvkid, uid, tvid, tvkustatus)
                result = self.build_tvkatalogues_attributes(tvkid, uid, tvid, tvkustatus)
                return jsonify(tvkatalogues=result), 200