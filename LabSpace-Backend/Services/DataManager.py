import sys
#sys.path.append("../../classes")
#from Configuration import SourceConfiguration
#from DataSource import DataBaseSource
from DBHelper import Connect
from flask import Flask, jsonify, json, request
from flask_cors import cross_origin
from collections import Counter
from sqlalchemy.sql import text
import pyodbc

app = Flask(__name__)
app.url_map.strict_slashes = False

# Service Functionality
@app.route('/DataManager')
@cross_origin()
def GetPerson():

    # Try
    try:
        # Connection Section        
        #config = SourceConfiguration("../config/datasource.config")
        #DataSource = DataBaseSource(config)
        #DataSource.TDSconfigure()
        Conn = Connect('postgres', 'Ghost!90', 'labspacedb')
        Response = Conn.execute("SELECT pgp_sym_decrypt(FirstName::bytea, 'longsecretencryptionkey') AS FirstName, pgp_sym_decrypt(lastname::bytea, 'longsecretencryptionkey') AS LastName,\
        pgp_sym_decrypt(netid::bytea, 'longsecretencryptionkey') AS NetId,  pgp_sym_decrypt(nsheid::bytea, 'longsecretencryptionkey')AS NSHE,\
        to_char(CreatedOn, 'HH12:MI:SS') createdon, to_char(modifiedon, 'HH12:MI:SS') modifiedon, IsDeleted, IsActive FROM Person")
        # row = crsr.fetchone()
        # print(row)


        # Retrieving Data
        Data = []
        # with open("../SQLQueries/MeasurementsByDatastream.sql") as r:
        #     Query = r.read()
        #     Query = text(Query)
        #     Measurements = DataSource.Connection.execute(Query,x=DatastreamID,y=Interval)

        # Processing Data
        Row = Response.fetchone()

        # Processing Each Measurement
        while Row is not None:
            StructuredData = {}
            StructuredData['FirstName'] = Row[0]
            StructuredData['LastName'] = Row[1]
            StructuredData['Netid'] = Row[2]
            StructuredData['NSHEID'] = [3]
            StructuredData['CreatedOn'] = [4]
            StructuredData['ModifiedOn'] = [5]
            StructuredData['IsDeleted'] = [6]
            StructuredData['IsActive'] = [7]
            Data.append(StructuredData)
            Row = Response.fetchone()

        # Close Connections
        Response.close()
        Conn.close()

        #return "Success"
        #Serialize
        return jsonify(Data)

    # Except
    except Exception as e:
        print(str(e))
        return False, str(e)


# Service Functionality
@app.route('/DataManager/Post')
@cross_origin()
def PostPerson():

    # Try
    try:
        # Connection Section        
        #config = SourceConfiguration("../config/datasource.config")
        #DataSource = DataBaseSource(config)
        #DataSource.TDSconfigure()
        Conn = Connect('postgres', 'Ghost!90', 'labspacedb')
        crsr = Conn.execute("SELECT pgp_sym_decrypt(FirstName::bytea, 'longsecretencryptionkey') AS FirstName, pgp_sym_decrypt(lastname::bytea, 'longsecretencryptionkey') AS LastName,\
        pgp_sym_decrypt(netid::bytea, 'longsecretencryptionkey') AS NetId,  pgp_sym_decrypt(nsheid::bytea, 'longsecretencryptionkey')AS NSHE,\
        to_char(CreatedOn, 'HH12:MI:SS') createdon, to_char(modifiedon, 'HH12:MI:SS') modifiedon, IsDeleted, IsActive FROM Person")
        row = crsr.fetchone()
        print(row)
        crsr.close()
        Conn.close()

        return "Success"

    # Except
    except Exception as e:
        print(str(e))
        return False, str(e)        

# Run Main
if __name__ == '__main__':
	# Set to False when deploying
	app.debug = False
	app.run(host='127.0.0.1', port=8081)