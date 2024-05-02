from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Web_Interaction:
    """
    This is used for Web Interaction with Selenium and all the
    web elements can be accessed via XPATH only
    """

    def __init__(self):
        self.driver = webdriver.Chrome()

    def NavigateTo(self, Url: str):
        """
        Navigate to particular website with Url mentioned
        :param Url: (str) : The URL to where the user wants to navigate
        :return: None
        """

        self.driver.get(Url)

    def ClickElement(self, Xpath : str):
        """
        It will click the web element present on Instance
        :param Xpath: (str) : The Xpath Locator for accessing Web Elements
        :return: None
        """

        self.driver.find_element(By.XPATH,Xpath).click()

    def WaitCustom(self, Seconds: int):
        """
        It will stop the program for user-defined number of seconds
        :param Seconds: (int) : An Integer to pass for number of sec
        :return: None
        """

        sleep(Seconds)

    def WaitMin(self):
        """
        It will wait for minimum of 1 second
        :return: None
        """

        sleep(1)

    def SendKeys(self,Key , Xpath : str):
        """
        It will send the keys to the input field to selenium web element
        :param Xpath: (str) : The Xpath Locator for accessing Web Elements
        :return: None
        """

        self.GetElement(Xpath).send_keys(Key)

    def GetElement(self, Xpath : str):
        """
        It will find the selenium element available on instance
        :param Xpath: (str) : The Xpath Locator for accessing Web Elements
        :return: (element) : The Selenium Element, otherwise None
        """

        if len(self.driver.find_elements(By.XPATH, Xpath)) > 0:
            return self.driver.find_elements(By.XPATH, Xpath)[0]

        else:
            print("No Element Found")
            return None

    def GetElementText(self, Xpath : str):
        """
        It will extract the text from the selenium web element available on instance
        :param Xpath: (str) : The Xpath Locator for accessing Web Elements
        :return: (str) : The text for that particular element, otherwise ''
        """

        if self.GetElement(Xpath) is not None:
            return self.GetElement(Xpath).text

        else:
            print("No Element Found")
            return ""

    def GetElemets(self, Xpath : str):
        """
        It will find the list of selenium web elements available on instance
        :param Xpath: (str) : The Xpath Locator for accessing Web Elements
        :return: (list) : The list of selenium web element, otherwise []
        """

        return self.driver.find_elements(By.XPATH,Xpath)