import csv
import pandas as pd
import json
from FilePath_OOP import FilePath

filePath_Json = FilePath("臺中市區公車路線圖", "JSON").path()
filePath_CSV = ""

class model:
    def __init__(self):
        
        self.Gov_DPM_ID = "機關代碼"
        self.Gov_DPM_Phone = "電話/市話"
        self.Data_Row_ID = "序號"

        self.Com_BusLine = "公車業者"
        self.BusLineID = "路線"
        self.BusLineName = "路線說明"
        self.BusLineImgLink = "連結"

        self.RoundTrip_ob = "去程"
        self.RoundTrip_ib = "回程"

        self.Remark = "備註"


    def readCSV_File(self):
        
        busList=[]             
        with open(filePath_CSV,newline='',encoding='utf-8-sig') as csvFile:   #encoding='utf-8-sig'     
            rows=csv.DictReader(csvFile)
            for row in rows:
                busList.append(row)                       
        csvFile.close()
        return busList
    
    def readJson_File(self):

        with open(filePath_Json,'r') as file:
            jsonFile = json.load(file)
        return jsonFile


