
# Real Estate Agent Scraper

Hi, I am Risala. 
This project is a web scraping tool built using the Scrapy framework in Python. The tool extracts detailed information about real estate agents listed on the [**Berkshire Hathaway HomeServices**](https://www.bhhsamb.com/roster/Agents) website and stores the data in CSV and JSON formats.

## Features

- **Website Scraped**: [Berkshire Hathaway HomeServices](https://www.bhhsamb.com/roster/Agents)
- **Extracted Data**:
  - **Name**: Full name of the agent
  - **Job Title**: Designation of the agent (e.g., Realtor, Broker, etc.)
  - **Image**: URL to the agent's profile picture
  - **Address**: Agent's location or office address
  - **Contact Details**: Includes phone numbers, emails, etc.
  - **Social Accounts**: Links to the agent’s social media profiles
  - **Offices**: List of offices associated with the agent
  - **Languages**: List of languages the agent can communicate in
  - **Description**: A brief bio or overview of the agent’s professional background
- **Data Outputs**:
  - CSV file
  - JSON file

## Output

The scraper successfully extracts more than 1,000 agent profiles and stores the data in two formats:
1. **CSV** - A structured, tabular format suitable for analysis.
2. **JSON** - A nested format that preserves data relationships for flexible usage.

The output files are stored in the `output` folder inside the `tutorial` directory:

- [CSV Output](tutorial/output/output.csv)
- [JSON Output](tutorial/output/output.json)

## Installation

1. **Install Python**:
   Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).

2. **Install Scrapy**:
   Install the Scrapy framework using `pip`:

    ```bash
    pip install scrapy
    ```

3. **Clone the Repository**:
   Clone the repository from GitHub and navigate to the `tutorial` directory:

    ```bash
    git clone https://github.com/risalarafic/myNew_Scrapy.git
    cd myNew_Scrapy/tutorial
    ```

For more information on Scrapy and how to get started, refer to the [Scrapy Documentation and Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html).

## Usage

To run the scraper:

```bash
scrapy crawl agent_spider -o output/output.json
```

You can also generate the data in CSV format:

```bash
scrapy crawl agent_spider -o output/output.csv
```

## Project Structure

```
C:.
│   outputtree.txt
│   scrapy.cfg
│   
├───output
│       example_output.json
│       output.csv
│       output.json
│       
└───tutorial
    │   items.py
    │   middlewares.py
    │   output.json
    │   outputcsv.csv
    │   pipelines.py
    │   requirement.txt
    │   settings.py
    │   __init__.py
    │   
    ├───spiders
    │   │   new.json
    │   │   newscrap.py
    │   │   output.csv
    │   │   quotes.jsonl
    │   │   tryscrapy.py
    │   │   __init__.py
    │   │   
    │   └───__pycache__
    │           mynewspider.cpython-312.pyc
    │           newscrap.cpython-312.pyc
    │           newww.cpython-312.pyc
    │           quotes_spider.cpython-312.pyc
    │           readablejson.cpython-312.pyc
    │           Roster_agents.cpython-312.pyc
    │           tryscrapy.cpython-312.pyc
    │           __init__.cpython-312.pyc
    │           
    └───__pycache__
            settings.cpython-312.pyc
            __init__.cpython-312.pyc
            

```

## Technologies Used

- **Python**: Programming language used for building the scraper.
- **Scrapy**: A fast and powerful web scraping framework.
- **CSV** & **JSON**: Data formats for outputting scraped data.

