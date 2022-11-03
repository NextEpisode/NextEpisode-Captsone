import pyodbc


class MovieKatalogueDAO:
    # fix this url crap tonightUID
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', moviekatalogue='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", moviekatalogue='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",
        SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #moviekataloguename = 'mymoviekataloguename' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+moviekataloguename+';PWD='+ password)
    #cursor = cnxn.cursor()

    def getAllMovieKatalogues(self):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue];"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMovieKatalogueById(self, MKID):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where MKID = ?;"
        cursor.execute(query, (MKID))
        result = cursor.fetchone()
        return result

    def getMovieKatalogueByUID(self, UID):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where uid = ?;"
        cursor.execute(query, (UID,))
        result = cursor.fetchone()
        return result

    def insert(self, uid, movieid, mkustatus):
        cursor = self.conn.cursor()
        query = "insert into [MovieKatalogue](uid, movieid, mkustatus) values (?, ?, ?) ;"
        cursor.execute(query, (uid, movieid, mkustatus))
        query = "SELECT @@IDENTITY AS [MKID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, MKID):
        cursor = self.conn.cursor()
        query = "delete from [MovieKatalogue] where MKID = ?;"
        cursor.execute(query, (MKID,))
        self.conn.commit()
        return MKID

    def update(self, MKID, uid, movieid, mkustatus):
        cursor = self.conn.cursor()
        query = "update [MovieKatalogue] set uid = ?, movieid = ?, mkustatus=? where MKID = ?;"
        cursor.execute(query, (uid, movieid, mkustatus, MKID))
        self.conn.commit()
        return MKID