from flask import jsonify
from dao import ForumDao


class ForumHandler:
    def build_forums_dict(self, row):
        result = {}
        result['FID'] = row[0]
        result['UID'] = row[1]
        result['FCategory'] = row[2]
        result['FName'] = row[3]
        return result

    def build_forums_attributes(self, FID, UID, FCategory, FName):
        result = {}
        result['FID'] = FID
        result['UID'] = UID
        result['FCategory'] = FCategory
        result['FName'] = FName
        return result

    def getAllForums(self):
        dao = ForumDao.ForumDAO()
        Forums_list = dao.getAllForums()
        result_list = []
        for row in Forums_list:
            result = self.build_forums_dict(row)
            result_list.append(result)
        return jsonify(Forums=result_list)

    def getForumById(self, json):
        FID = json['FID']
        dao = ForumDao.ForumDAO()
        row = dao.getForumById(FID)
        if not row:
            return jsonify(Error = "Forum Not Found"), 404
        else:
            Forums = self.build_forums_dict(row)
            return jsonify(Forums = Forums)

    def insertForumJson(self, json):
            uid = json['UID']
            fcategory =json['FCategory']
            fname = json['FName']
            if uid and fcategory and fname:
                dao = ForumDao.ForumDAO()
                fid = dao.insert(uid, fcategory, fname)
                result = self.build_forums_attributes(fid, uid, fcategory, fname)
                return jsonify(Forums=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteForum(self, fid):
        dao = ForumDao.ForumDAO()
        if not dao.getForumById(fid):
            return jsonify(Error = "Forum not found."), 404
        else:
            dao.delete(fid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateForumJson(self, fid, json):
        dao = ForumDao.ForumDAO()
        if not dao.getForumById(fid):
            return jsonify(Error="Forum not found."), 404
        else:
            uid = json['UID']
            fcategory =json['FCategory']
            fname = json['FName']
            if uid and fcategory and fname:
                dao.update(uid, fcategory, fname)
                result = self.build_forums_attributes(fid, uid, fcategory, fname)
                return jsonify(Forums=result), 200