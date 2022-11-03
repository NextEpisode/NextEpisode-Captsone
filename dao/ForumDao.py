from asyncio.windows_events import NULL
from contextlib import nullcontext
import pyodbc
from flask import jsonify

class ForumDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', forum='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", forum='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",
        SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #forumname = 'myforumname' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+forumname+';PWD='+ password)
    #cursor = cnxn.cursor()


    def getAllForums(self):
        cursor = self.conn.cursor()
        query = "select * from Forums;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getForumById(self, FID):
        cursor = self.conn.cursor()
        query = "select * from [Forums] Where fid = ?;"
        cursor.execute(query, (FID,))
        result = cursor.fetchone()
        return result

    def insert(self, uid, fcategory, fname):
        cursor = self.conn.cursor()
        query = "insert into [Forums](uid, fcategory, fname) values (?, ?, ?) ;"
        cursor.execute(query, (uid, fcategory, fname))
        query = "SELECT @@IDENTITY AS [FID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, FID):
        cursor = self.conn.cursor()
        query = "delete from [Forums] where fid = ?;"
        cursor.execute(query, (FID,))
        self.conn.commit()
        return FID

    def update(self, fid, uid, fcategory, fname):
        cursor = self.conn.cursor()
        query = "update [forums] set uid = ?, fcategory = ?, fname =? where fid = ?;"
        cursor.execute(query, (uid, fcategory, fname, fid))
        self.conn.commit()
        return fid