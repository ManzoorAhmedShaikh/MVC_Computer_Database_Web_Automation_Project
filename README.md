# Computer Database MVC (Scraper & Modifier)

## Description
The **Computer Database MVC (Scraper & Modifier)** project leverages the power of Python and Selenium to interact with [Computer Database](https://computer-database.gatling.io/). It is designed to perform two main operations:

1. **Scraping:** Users can scrape data about computers, either selectively or entirely from the database. The scraped data can be exported in various formats including Excel, CSV, or JSON.
2. **Automating:** The project allows users to automate the addition of new computers to the database via an input file provided in Excel or CSV format. Computers to be added should have their status set to "Configure" within the input file.

Built using the MVC (Model-View-Controller) architecture, this project includes:
- **Models** for Selenium interactions, data import, and flag handling.
- **Views** for data export.
- **Controller** for orchestrating operations based on user-configured flags in the `init` file.

## Key Features
- **Scrape Data by Quantity:** Extract specified number of computer records.
- **Scrape All Data:** Extract all computer records from the database.
- **Configure Multiple Objects:** Add multiple computer records through a single input file.

## Installation
Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/ManzoorAhmedShaikh/MVC_Computer_Database_Web_Automation_Project.git]
cd [MVC_Computer_Database_Web_Automation_Project]
pip install selenium pandas openpyxl
