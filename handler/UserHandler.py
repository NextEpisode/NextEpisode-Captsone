from flask import jsonify
from dao import UserDao


class UserHandler:
    def build_users_dict(self, row):
        result = {}
        result['UID'] = row[0]
        result['GoogleID']=row[1]
        result['KID']=row[2]
        result['UName'] = row[3]
        return result

    def build_users_attributes(self, UID, GoogleID, KID, UName):
        result = {}
        result['UID'] = UID
        result['GoogleID']=GoogleID
        result['KID']=KID
        result['UName'] = UName
        return result

    def getAllUsers(self):
        dao = UserDao.UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_users_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, json):
        UID = json['UID']
        dao = UserDao.UserDAO()
        row = dao.getUserById(UID)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)
        
    def getUserByGoogleId(self, json):
        googleid = json['GoogleID']
        dao = UserDao.UserDAO()
        row = dao.getUserByGoogleId(googleid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            users = self.build_users_dict(row)
            return jsonify(Users = users)
        
    def insertUserJson(self, json):
            googleid = json['GoogleID']
            uname = json['UName']
            dao = UserDao.UserDAO()
            row = dao.getUserByGoogleId(googleid)
            if row:
                return jsonify(Error = "User Exists"), 404
            else:
                if uname and googleid:
                    uid = dao.insert(googleid, uname)
                    kid = dao.getUserKID(uid)
                    result = self.build_users_attributes(uid, googleid, kid, uname)
                    return jsonify(Users=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUserJson(self, json):
        dao = UserDao.UserDAO()
        googleid = json['GoogleID']
        uname = json['UName']
        if not dao.getUserByGoogleId(googleid):
            return jsonify(Error="User not found."), 404
        else:
            if uname and googleid:
                dao.update(googleid, uname)
                uid = dao.getUserUID(googleid)
                kid = dao.getUserKID(uid)
                result = self.build_users_attributes(uid, googleid, kid, uname)
                return jsonify(Users=result), 200

    def deleteUser(self, json):
        dao = UserDao.UserDAO()
        googleid = json["GoogleID"]
        if not dao.getUserByGoogleId(googleid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.delete(googleid)
            return jsonify(DeleteStatus = "OK"), 200