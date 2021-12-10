import sys
from random import random
from abc import ABCMeta, abstractmethod
#from Configuration import SourceConfiguration
#from DataContainers import DataStream, Measurement
from sqlalchemy import create_engine, text
import pyodbc
import urllib

class DataSource:
    __metaclass__ = ABCMeta

    def __init__(self, configuration = None):
        self.configuration = configuration

    @abstractmethod
    def configure(self):
        return False

    @abstractmethod
    def read(self):
        return False

    @abstractmethod
    def write(self):
        return False

def Connect(User,Pass,Db):
    ConnStr ="DRIVER={PostgreSQL ODBC Driver(UNICODE)};Server=127.0.0.1;Database="+ Db +";UID="+ User +";PWD="+ Pass +";Port=5432;"
    Conn = pyodbc.connect(ConnStr)
    return Conn


class DataBaseSource(DataSource):

    def __init__(self, configuration = None):
        self.Configuration = configuration
        self.Engine = None
        self.Connection = None
        self.ConnectionString = ""


    def configure(self):
        #retrieve configuration dictionary
        ConfigDOM = self.Configuration.SourceMetaData

        #get connection string
        ConnString = ConfigDOM.getElementsByTagName("Connection")[0].firstChild.nodeValue;

        #build connection string
        ConnString = ConnString.format(ConfigDOM.getElementsByTagName("Username")[0].firstChild.nodeValue, ConfigDOM.getElementsByTagName("Password")[0].firstChild.nodeValue, ConfigDOM.getElementsByTagName("Name")[0].firstChild.nodeValue)

        self.ConnectionString = ConnString;

        #generate connection and bind to class
        self.Engine = create_engine(ConnString)
        self.Connection = self.Engine.connect()

    def TDSconfigure(self):

        # Extract User, Pass, and Db Name from DOM
        ConfigDOM = self.Configuration.SourceMetaData
        User = ConfigDOM.getElementsByTagName("Username")[0].firstChild.nodeValue
        Pass = ConfigDOM.getElementsByTagName("Password")[0].firstChild.nodeValue
        Db = ConfigDOM.getElementsByTagName("Name")[0].firstChild.nodeValue

        # Form TDS connection string
        quoted = urllib.parse.quote_plus("DRIVER={PostgreSQL Unicode(x64)};Server=localhost;Database="+ Db +";UID="+ User +";PWD="+ Pass +";TDS_Version=8.0;Port=1433;")
        self.Engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(quoted))
        self.Connection = self.Engine.connect()


    def read(self, SQLQuery):
        QueryResponse = self.Connection.execute(SQLQuery)
        return QueryResponse

    def write(self):
        return False    

    def write(self, SQLQuery):
        self.Connection.execute(SQLQuery)
