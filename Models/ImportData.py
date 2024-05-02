import os
import pandas as pd

class ImportData:

    def ReadCSVXLSX(self, FileFormat : str):
        """
        It is used to read either 1 CSV or EXCEL file from the Inputs Directory
        :param FileFormat: (str) : A string to decide the file extension, either 'csv' or 'xlsx'
        :return: Data (dict) : A single dimensional dictionary containing data for the Input
        """

        Data = []
        try:
            if "Inputs" in os.listdir():

                if FileFormat.lower() == 'csv':
                    Files = [file for file in os.listdir('Inputs') if file.endswith('.csv')]

                elif FileFormat.lower() == 'xlsx':
                    Files = [file for file in os.listdir('Inputs') if file.endswith('.xlsx')]

                else:
                    print("Invalid File format, kindly verify.")
                    Files = None

                if Files is not None:
                    if FileFormat.lower() == 'csv':
                        Data = pd.read_csv("Inputs/" + Files[0])
                    else:
                        Data = pd.read_excel("Inputs/" + Files[0])

                    print(f"File: {Files[0]} imported successfully.")
                    Data.fillna('',inplace = True) #To replace nan with empty string
                    Data['Computer Name'] = Data['Computer Name'].str.strip() #To remove any irrelavant data of some spaces, since it is MANDATORY FIELD
                    Data = dict(Data[(Data['Status'] == "Configure") & (Data["Computer Name"] != '')]) # Filtering what to process and what not to
                    return Data

                else:
                    return Data

            else:
                print("Input folder is not present, therefore no data can be imported.")
                return Data

        except Exception as error:
            print(f"Error in Importing Data from CSV/XLSX file -> Exception: {error}")
            return Data