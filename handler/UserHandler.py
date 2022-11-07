from flask import jsonify
from dao import UserDao


class UserHandler:
    def build_users_dict(self, row):
        result = {}
        result['UID'] = row[0]
        result['UName'] = row[1]
        result['GoogleID']=row[2]
        return result

    def build_users_attributes(self, UID, UName, GoogleID):
        result = {}
        result['UID'] = UID
        result['UName'] = UName
        result['GoogleID']= GoogleID
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
            uname = json['UName']
            googleid = json['GoogleID']
            dao = UserDao.UserDAO()
            row = dao.getUserByGoogleId(googleid)
            if row:
                return jsonify(Error = "User Exists"), 404
            else:
                if uname and googleid:
                    uid = dao.insert(uname, googleid)
                    result = self.build_users_attributes(uid, uname, googleid)
                    return jsonify(Users=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUserJson(self, json):
        dao = UserDao.UserDAO()
        uid = json["UID"]
        uname = json['UName']
        googleid = json['GoogleID']
        if not dao.getUserByGoogleId(googleid):
            return jsonify(Error="User not found."), 404
        else:
            if uid and uname and googleid:
                dao.update(uid, uname, googleid)
                result = self.build_users_attributes(uid, uname, googleid)
                return jsonify(Users=result), 200

    def deleteUser(self, uid):
        dao = UserDao.UserDAO()
        if not dao.getUserById(uid):
            return jsonify(Error = "User not found."), 404
        else:
            dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200