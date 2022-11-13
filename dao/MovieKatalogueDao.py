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
    
    def getMovieKataloguesByKID(self, kid):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where kid = ?;"
        cursor.execute(query, (kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMovieKataloguesByStatus(self, KID, status):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where KID = ? and mkustatus = ?;"
        cursor.execute(query, (KID, status))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getMovieKatalogueByKID(self, kid, movieid):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where kid = ? and movieid = ?;"
        cursor.execute(query, (kid, movieid))
        result = cursor.fetchone()
        return result
    
    def getExistingEntry(self, kid, movieid):
        cursor = self.conn.cursor()
        query = "select * from [MovieKatalogue] Where kid = ? and movieid = ?;"
        cursor.execute(query, (kid, movieid))
        result = cursor.fetchone()
        return result

    def insert(self, kid, movieid, mkustatus):
        cursor = self.conn.cursor()
        query = "insert into [MovieKatalogue](kid, movieid, mkustatus) values (?, ?, ?) ;"
        cursor.execute(query, (kid, movieid, mkustatus))
        query = "SELECT @@IDENTITY AS [MKID];"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.commit()
        return result

    def delete(self, kid, movieid):
        cursor = self.conn.cursor()
        query = "delete from [MovieKatalogue] where kid = ? and movieid = ?;"
        cursor.execute(query, (kid, movieid))
        self.conn.commit()
        return kid
    
    def deleteAll(self, KID):
        cursor = self.conn.cursor()
        query = "delete from [MovieKatalogue] where kid = ?;"
        cursor.execute(query, (KID))
        self.conn.commit()
        return KID

    def update(self, kid, movieid, mkustatus):
        cursor = self.conn.cursor()
        query = "update [MovieKatalogue] set mkustatus=? where movieid =? and kid = ?;"
        cursor.execute(query, (mkustatus, movieid, kid))
        self.conn.commit()
        return kid