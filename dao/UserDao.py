from asyncio.windows_events import NULL
from contextlib import nullcontext
import pyodbc
from flask import jsonify


class UserDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', user='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", user='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",
        SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #username = 'myusername' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    #cursor = cnxn.cursor()


    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from [Users];"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, UID):
        cursor = self.conn.cursor()
        query = "select * from [Users] Where uid = ?;"
        cursor.execute(query, (UID,))
        result = cursor.fetchone()
        return result

    def getUserByGoogleId(self, googleid):
        cursor = self.conn.cursor()
        query = "select * from [Users] Where googleid = ?;"
        cursor.execute(query, (googleid,))
        result = cursor.fetchone()
        return result
    
    def getUserKID(self, uid):
        cursor = self.conn.cursor()
        query = "select KID from [Users] Where uid = ?;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()[0]
        return result
    
    def getUserUID(self, gid):
        cursor = self.conn.cursor()
        query = "select UID from [Users] Where googleid = ?;"
        cursor.execute(query, (gid,))
        result = cursor.fetchone()[0]
        return result

    def insert(self, googleid, uname):
        cursor = self.conn.cursor()
        query = "insert into [Users](GoogleID, UName) values (?, ?);"
        cursor.execute(query, (googleid, uname))
        query = "SELECT @@IDENTITY AS [UID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, gid):
        cursor = self.conn.cursor()
        query = "delete from [Users] where googleid = ?;"
        cursor.execute(query, (gid,))
        self.conn.commit()
        return gid

    def update(self, googleid, uname):
        cursor = self.conn.cursor()
        query = "update [Users] set uname = ? where googleid = ?;"
        cursor.execute(query, (uname, googleid))
        self.conn.commit()
        return googleid

    def lastInsert(self):
        cursor = self.conn.cursor()
        query = "SELECT @@IDENTITY AS [UID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        return result