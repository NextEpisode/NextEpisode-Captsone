import pyodbc


class ForumCommentDAO:
    # fix this url crap tonight
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', forum='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", forum='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", forum='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #forumname = 'myforumname' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+forumname+';PWD='+ password)
    #cursor = cnxn.cursor()


    def getAllForumComments(self):
        cursor = self.conn.cursor()
        query = "select * from [ForumComment];"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getForumCommentById(self, FCID):
        cursor = self.conn.cursor()
        query = "select * from [ForumComment] Where fcid = ?;"
        cursor.execute(query, (FCID,))
        result = cursor.fetchone()
        return result

    def insert(self, fid, uid, fctext):
        cursor = self.conn.cursor()
        query = "insert into [ForumComment](fid, uid, fctext) values (?, ?, ?);"
        cursor.execute(query, (fid, uid, fctext))
        query = "SELECT @@IDENTITY AS [FCID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, FCID):
        cursor = self.conn.cursor()
        query = "delete from [ForumComment] where fcid = ?;"
        cursor.execute(query, (FCID,))
        self.conn.commit()
        return FCID

    def update(self, fcid, fid, uid, fctext):
        cursor = self.conn.cursor()
        query = "update [ForumComment] set fid=?,  uid = ?, fctext = ? where fcid = ?;"
        cursor.execute(query, (fid, uid, fctext, fcid))
        self.conn.commit()
        return fcid