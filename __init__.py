from Controllers.Main_Controller import Main_Controller
from Models.Flags import Flags, FlagsType

if __name__ == "__main__":
    """
    Kindly Enable either any one of the condition, Scrap or Configure, 
    if both are uncomment then only the Scrap part will be executed
    """

    #Operation_Type_____________________
    # FlagsType.RunScrap = True
    FlagsType.RunConfig = True
    #____________________________________

    #Scraper_____________________________
    # Flags.RunScrap_ScrapByQuantity = True
    # Flags.RunScrap_ScrapAll = True
    #____________________________________

    #Configure___________________________
    Flags.RunConfig_ConfigureWithExcelCSV = True
    #____________________________________

    print("Execution Started!...")
    Main_Controller().Run()
    print("Execution Ended!...")
