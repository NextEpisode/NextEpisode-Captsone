import pyodbc


class TVKatalogueDAO:
    # fix this url crap tonightUID
   ## def __init__(self):
   ##     connection_url = MySQLdb.connect(host='24.54.205.36', tvkatalogue='RemoteMatcha', passwd='RemoteMatcha', db='BeyondHorizonsDB',port = 6606)
   ##     # connection_url = (host="localhost", tvkatalogue='Argent', passwd='ArgentSable776', db='MatchaWareDB')
   ##     self.conn = connection_url

    def __init__(self):
        connection_url = pyodbc.connect(Driver="SQL Server Native Client 11.0",
        SERVER="localhost", DATABASE="BingeWatcherFlaskTest", Trusted_Connection="yes")
        ##connection_url = MySQLdb.connect(host="localhost", user='root', passwd='root', db='BeyondHorizonsDB')
        self.conn = connection_url

    #server = 'tcp:myserver.database.windows.net' 
    #database = 'mydb' 
    #tvkataloguename = 'mytvkataloguename' 
    #password = 'mypassword' 
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    #cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+tvkataloguename+';PWD='+ password)
    #cursor = cnxn.cursor()


    def getAllTVKatalogues(self):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue];"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTVKataloguesByKID(self, kid):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] Where kid = ?;"
        cursor.execute(query, (kid))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getTVKataloguesByKIDTVID(self, kid, tvid):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] Where kid = ? and tvid = ?;"
        cursor.execute(query, (kid, tvid))
        result = cursor.fetchone()
        return result


    def getAllTVKataloguesByStatus(self, kid, status):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] where kid = ? and tvkustatus = ?;"
        cursor.execute(query, (kid, status))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getExistingEntry(self, kid, tvid):
        cursor = self.conn.cursor()
        query = "select * from [TVKatalogue] Where kid = ? and tvid = ?;"
        cursor.execute(query, (kid, tvid))
        result = cursor.fetchone()
        return result

    def insert(self, kid, tvid, tvkustatus, tvkuseason, tvkuepisode):
        cursor = self.conn.cursor()
        query = "insert into [TVKatalogue](kid, tvid, tvkustatus, tvkuseason, tvkuepisode) values (?, ?, ?,?,?) ;"
        cursor.execute(query, (kid, tvid, tvkustatus, tvkuseason, tvkuepisode))
        cursor.commit()
        return kid
    
    def updateKatalogue(self, kid, tvid, tvkustatus, tvkuseason, tvkuepisode):
        cursor = self.conn.cursor()
        query = "update [TVKatalogue] set tvkustatus = ?, tvkuseason = ?, tvkuepisode = ? where tvid = ? and kid=?;"
        cursor.execute(query, (tvkustatus, tvkuseason, tvkuepisode, tvid, kid))
        cursor.commit()
        return kid

    def updateStatus(self, tvkid, kid, tvid, tvkustatus):
        cursor = self.conn.cursor()
        query = "update [TVKatalogue] set tvkustatus = ? where tvid = ? and kid=?;"
        cursor.execute(query, (tvkustatus, tvid, kid))
        cursor.commit()
        return tvkid
    
    def updateSeason(self, tvkid, kid, tvid, tvkuseason):
        cursor = self.conn.cursor()
        query = "update [TVKatalogue] set tvkuseason = ?where tvid = ? and kid=?;"
        cursor.execute(query, (tvkuseason,tvid, kid))
        cursor.commit()
        return tvkid
    
    def updateEpisode(self, tvkid, kid, tvid, tvkuepisode):
        cursor = self.conn.cursor()
        query = "update [TVKatalogue] set tvkuepisode = ? where tvid = ? and kid=?;"
        cursor.execute(query, (tvkuepisode, tvid, kid))
        cursor.commit()
        return tvkid
    
    def delete(self, kid, tvid):
        cursor = self.conn.cursor()
        query = "delete from [TVKatalogue] where kid = ? and tvid = ?;"
        cursor.execute(query, (kid, tvid))
        self.conn.commit()
        return kid
    
    def deleteAll(self, KID):
        cursor = self.conn.cursor()
        query = "delete from [TVKatalogue] where kid = ?;"
        cursor.execute(query, (KID))
        self.conn.commit()
        return KID

    #Make 3. Updates each one separately. 