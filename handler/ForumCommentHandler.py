from flask import jsonify
from dao import ForumCommentDao


class ForumCommentHandler:
    def build_forumcomments_dict(self, row):
        result = {}
        result['FCID'] = row[0]
        result['FID'] = row[1]
        result['UID'] = row[2]
        result['FCText'] = row[3]
        return result

    def build_forumcomments_attributes(self, FCID,  FID, UID, FCText):
        result = {}
        result['FCID'] = FCID
        result['FID'] = FID
        result['UID'] = UID
        result['FCText'] = FCText
        return result

    def getAllForumComments(self):
        dao = ForumCommentDao.ForumCommentDAO()
        Forums_list = dao.getAllForumComments()
        result_list = []
        for row in Forums_list:
            result = self.build_forumcomments_dict(row)
            result_list.append(result)
        return jsonify(ForumComments=result_list)

    def getForumCommentById(self, json):
        FCID = json['FCID']
        dao = ForumCommentDao.ForumCommentDAO()
        row = dao.getForumCommentById(FCID)
        if not row:
            return jsonify(Error = "ForumComment Not Found"), 404
        else:
            Forums = self.build_forumcomments_dict(row)
            return jsonify(Forums = Forums)

    def insertForumCommentJson(self, json):
            fid =json['FID']
            uid = json['UID']
            fctext =json['FCText']
            if fid and uid and fctext:
                dao = ForumCommentDao.ForumCommentDAO()
                fcid = dao.insert(fid, uid, fctext)
                result = self.build_forumcomments_attributes(fcid, fid, uid, fctext)
                return jsonify(Forums=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteForum(self, fid):
        dao = ForumCommentDao.ForumCommentDAO()
        if not dao.getForumCommentById(fid):
            return jsonify(Error = "Forum not found."), 404
        else:
            dao.delete(fid)
            return jsonify(DeleteStatus = "OK"), 200

    def updateForumJson(self, json):
        dao = ForumCommentDao.ForumCommentDAO()
        fcid = json["FCID"]
        fid = json["FID"]
        uid = json["UID"]
        fctext = ["FCText"]
        if not dao.getForumCommentById(fcid):
            return jsonify(Error="Comment not found."), 404
        else:
            if fcid and fid and uid and fctext:
                dao.update(fcid, fid, uid, fctext)
                result = self.build_forumcomments_attributes(fcid, fid, uid, fctext)
                return jsonify(Forums=result), 200