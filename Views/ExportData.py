import pandas as pd
import os
import time
import json

class ExportData:

    def ExportCSVXLSX(self, Data: list, FileName = str(time.strftime("%d%m%y%H%M%S",time.localtime())) + "_Output", FileFormat = 'csv'):
        """
        It is used to export the Data fetched from Instance in either CSV or XLSX file with Headers
        :param Data: (list) : A list of Dictionary that contains the Instance Data
        :param FileName: (str) : File name in string, if nothing pass, Default "Output" name will be considered
        :param FileFormat: (str) : A string to decide the file extension, either 'csv' or 'xlsx'
        :return: None
        """

        try:
            if len(Data) > 0:
                if "Outputs" not in os.listdir():
                    print("Output Directory not present, Making it!...")
                    os.makedirs("Outputs")

                Dataframe = pd.DataFrame(Data)
                Dataframe.fillna('', inplace = True)
                if FileFormat.lower() == 'csv':
                    Dataframe.to_csv("Outputs/" + FileName + "." + FileFormat.lower(), index_label='S.No')
                    print(f"Exported File: {FileName + '.' + FileFormat.lower()} Successfully")

                elif FileFormat.lower() == "xlsx":
                    Dataframe.to_excel("Outputs/" + FileName + "." + FileFormat.lower(), index_label='S.No')
                    print(f"Exported File: {FileName + '.' + FileFormat.lower()} Successfully")

                else:
                    print(f"Invalid File Format: '{FileFormat}', Kindly verify")

            else:
                print("Data is not fetched properly, Kindly verify!")

        except Exception as error:
            print(f"Error in Exporting CSV/XLSX file -> Exception: {error}")

    def ExportJSON(self, Data: list, FileName = str(time.strftime("%d%m%y%H%M%S",time.localtime())) + "_Output"):
        """
        It is used to export the Data fetched from Instance in the JSON file
        :param Data: (list) : A list of Dictionary that contains the Instance Data
        :param FileName: (str) : File name in string, if nothing pass, Default "Output" name will be considered
        :return: None
        """

        try:
            if len(Data) > 0:
                if "Outputs" not in os.listdir():
                    print("Output Directory not present, Making it!...")
                    os.makedirs("Outputs")

                JsonData = json.dumps(Data)
                with open("Outputs/" + FileName + ".json",'w') as File:
                    File.write(JsonData)
                    print(f"Exported File: {FileName + '.json'} Successfully")

            else:
                print("Data is not fetched properly, Kindly verify!")

        except Exception as error:
            print(f"Error in Exporting JSON file -> Exception: {error}")
