from Models.Web_Interaction import Web_Interaction
from Models.Flags import Flags,FlagsType
from Models.ImportData import ImportData
from Views.ExportData import ExportData
import calendar

class Main_Controller:

    def __init__(self):
        Flags()
        self.driver = Web_Interaction()
        self.Export = ExportData()
        self.driver.NavigateTo("https://computer-database.gatling.io/computers")

    def Run(self):

        if FlagsType.RunScrap:
            Data = []
            if Flags.RunScrap_ScrapByQuantity:
                Data = self.ScrapByQuantity(Numbers = 8)

            elif Flags.RunScrap_ScrapAll:
                Data = self.ScrapAll()

            else:
                print("Kindly select any flag from Scraping section, No Operation Executed!")
                return

            self.Export.ExportCSVXLSX(Data, FileName="MYTEST", FileFormat='XLsx')
            self.Export.ExportJSON(Data)

        elif FlagsType.RunConfig:

            if Flags.RunConfig_ConfigureWithExcelCSV:
                self.ConfigureObject()

            else:
                print("Kindly select any flag from Co section, No Operation Executed!")
                return

    def ScrapByQuantity(self, Numbers : int):
            """
            It will scrap Data according to the given "Numbers"
            :return: (list) : It will return a list of Dictionaries where each row represent 1 object
            """

            FinalData_List = []
            Month_dict = {month: index for index, month in enumerate(calendar.month_abbr) if month}
            Table_path = '//table[@class="computers zebra-striped"]/tbody'
            TotalRowsPerPage_path = Table_path + '/tr'
            ComputerName_path = Table_path + "/tr[{0}]/td[1]/a"
            Introduced_path = Table_path + "/tr[{0}]/td[2]"
            Discontinued_path = Table_path + "/tr[{0}]/td[3]"
            Company_path = Table_path + "/tr[{0}]/td[4]"
            NextBtn_path = '//li[@class="next"]//a'

            try:
                while (len(FinalData_List) <= Numbers):
                    TotalRows = len(self.driver.GetElemets(TotalRowsPerPage_path))
                    if TotalRows > 0:
                        for index in range(1, TotalRows + 1):

                            ComputerName = self.driver.GetElementText(ComputerName_path.format(index))

                            Introduced = ""
                            if self.driver.GetElementText(Introduced_path.format(index)) != "-":
                                Day,Month,Year = self.driver.GetElementText(Introduced_path.format(index)).split()
                                Month = Month_dict[Month] if Month_dict[Month] in ['10','11', '12'] else str(0) + str(Month_dict[Month])
                                Introduced = str(Year) + "-" + str(Month) + "-" + str(Day)

                            Discontinued = ""
                            if self.driver.GetElementText(Discontinued_path.format(index)) != "-":
                                Day,Month,Year = self.driver.GetElementText(Discontinued_path.format(index)).split()
                                Month = Month_dict[Month] if Month_dict[Month] in ['10','11', '12'] else str(0) + str(Month_dict[Month])
                                Discontinued = str(Year) + "-" + str(Month) + "-" + str(Day)

                            Company = self.driver.GetElementText(Company_path.format(index)) if self.driver.GetElementText(Company_path.format(index)) != "-" else ""

                            print(f"Computer Name: {ComputerName} | Introduced: {Introduced} | Discontinued: {Discontinued} | Company: {Company}")
                            FinalData_List.append({"Computer Name" : ComputerName,
                                                   "Introduced" : Introduced,
                                                   "Discontinued" : Discontinued,
                                                   "Company" : Company,
                                                   "Status": "Nothing"})

                        print("Clicking to Next Page Button!...")
                        self.driver.ClickElement(NextBtn_path)
                        self.driver.WaitMin()

                    else:
                        print("No Records Available")
                        return FinalData_List

                if len(FinalData_List) > Numbers:
                    print(f"Total Records Fetched: {len(FinalData_List)} and expected are: {Numbers}, So Removing Last: {len(FinalData_List) - Numbers} Records")
                    _ = [FinalData_List.pop() for index in range(len(FinalData_List) - Numbers)]

                return FinalData_List

            except Exception as error:
                print(f"Error in Fetching Data 'ScrapByQuantity()' -> Exception: '{error}'")
                return FinalData_List

    def ScrapAll(self):
        """
        It will scrap Complete Computer Database from the Instance
        :return: (list) : It will return a list of Dictionaries where each row represent 1 object
        """

        FinalData_List = []
        Month_dict = {month: index for index, month in enumerate(calendar.month_abbr) if month}
        Table_path = '//table[@class="computers zebra-striped"]/tbody'
        TotalRowsPerPage_path = Table_path + '/tr'
        ComputerName_path = Table_path + "/tr[{0}]/td[1]/a"
        Introduced_path = Table_path + "/tr[{0}]/td[2]"
        Discontinued_path = Table_path + "/tr[{0}]/td[3]"
        Company_path = Table_path + "/tr[{0}]/td[4]"
        NextBtn_path = '//li[@class="next"]//a'
        TotalRecordsOnInstance_path = '//h1[not(@class)]'

        try:
            TotalRecords = int(self.driver.GetElementText(TotalRecordsOnInstance_path).split()[0])
            while len(FinalData_List) <= TotalRecords:
                TotalRows = len(self.driver.GetElemets(TotalRowsPerPage_path))
                if TotalRows > 0:

                    for index in range(1, TotalRows + 1):
                        ComputerName = self.driver.GetElementText(ComputerName_path.format(index))

                        Introduced = ""
                        if self.driver.GetElementText(Introduced_path.format(index)) != "-":
                            Day,Month,Year = self.driver.GetElementText(Introduced_path.format(index)).split()
                            Month = Month_dict[Month] if Month_dict[Month] in ['10','11', '12'] else str(0) + str(Month_dict[Month])
                            Introduced = str(Year) + "-" + str(Month) + "-" + str(Day)

                        Discontinued = ""
                        if self.driver.GetElementText(Discontinued_path.format(index)) != "-":
                            Day,Month,Year = self.driver.GetElementText(Discontinued_path.format(index)).split()
                            Month = Month_dict[Month] if Month_dict[Month] in ['10','11', '12'] else str(0) + str(Month_dict[Month])
                            Discontinued = str(Year) + "-" + str(Month) + "-" + str(Day)

                        Company = self.driver.GetElementText(Company_path.format(index)) if self.driver.GetElementText(Company_path.format(index)) != "-" else ""

                        print(f"Computer Name: {ComputerName} | Introduced: {Introduced} | Discontinued: {Discontinued} | Company: {Company}")
                        FinalData_List.append({"Computer Name": ComputerName,
                                               "Introduced": Introduced,
                                               "Discontinued": Discontinued,
                                               "Company": Company})

                    self.driver.ClickElement(NextBtn_path)
                    self.driver.WaitMin()

                else:
                    print("No more records Available!")
                    return FinalData_List

            return FinalData_List

        except Exception as error:
            print(f"Error in Fetching Data 'ScrapAll()' -> Exception: '{error}'")
            return FinalData_List

    def ConfigureObject(self):

        AddNewComputer_path = '//a[@id="add"]'
        Fields_path = "//label[text() = '{0}']/following-sibling::div/input"
        Dropdown_path = "//label[text() = 'Company']/following-sibling::div/select/option[.='{0}']"
        CreateComputerBtn_path = "//input[@type='submit']"

        try:
            Data = ImportData.ReadCSVXLSX(self, FileFormat = 'XLSX')

            for i in range(len(Data['Status'].values)):
                self.driver.ClickElement(AddNewComputer_path)
                self.driver.WaitMin()

                print(f"Filling fields for Computer: {Data['Computer Name'].values[i]}")
                self.driver.SendKeys(Data['Computer Name'].values[i], Fields_path.format('Computer name'))
                self.driver.SendKeys(Data['Introduced'].values[i], Fields_path.format('Introduced'))
                self.driver.SendKeys(Data['Discontinued'].values[i], Fields_path.format('Discontinued'))
                self.driver.ClickElement(Dropdown_path.format(Data['Company'].values[i])) if Data['Company'].values[i] != "" else ""
                print("Saving Changes")

                self.driver.ClickElement(CreateComputerBtn_path)
                self.driver.WaitMin()

        except Exception as error:
            print(f"Error in Configuring in 'ConfigureObject()' -> Exception: '{error}'")
