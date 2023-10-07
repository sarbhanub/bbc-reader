[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

# BBC Reader

BBC Reader is a web-app that is built around the database which is being craeted by BBC Scraper. It is storing scraped data to MongoDB multiple times a day. More about the 'bbc-scraper' project below.

## See the app in action 

Open on Deta [(link)](https://bbcreader-1-r8262778.deta.app)\
Open on Render (Slower) [(link)](https://bbc-reader.onrender.com)

## Features

- Built around flask web framework.
- Uses MongoDB as the source database.
- Optimized web interface suitable for easy reading.
- User friendly interface.

## Used Frameworks and Libraries

Flask, PyMongo, Web (HTML, CSS, Vanila JS)

## Sample Page

![Screenshot](screenshots/bbc-reader-20230910.png "Sample page on 2023-09-10")

## Disclaimer

Please note that scraping websites may be subject to legal restrictions or terms of service. Make sure to review and comply with any applicable terms and conditions when using this web-app. BBC Reader is provided as-is and the developers are not responsible for any misuse or legal consequences resulting from its use.

# BBC Scraper 

[Link](https://github.com/sarbhanub/bbc-scraper) (Private)

This repository contains a scraper built with Python and integrated with GitHub Actions to fetch RSS feeds from BBC multiple times a day. The scraper utilizes the power of GitHub Actions to automate the scraping process.

## Features

- Fetches 16 public RSS feeds from BBC. (feeds/rss.csv)
- Runs the scraper 8 times a day to keep the news articles up to date.
- Utilizes GitHub Actions for automation and scheduling.
- Saves scraped data to a MongoAtlas cluster. Additionally, saves polarity/sentiment of each article fetched as well.

## Project Structure

The basic project structure is as follows:
```bash
root\
  ├─ .github\
  │  └─ workflows\
  │     └─ actions.yml
  ├─ .gitignore
  ├─ feeds\
  │  └─ rss.csv
  ├─ resources\
  │  └─ nltk_data\
  │     └─ sentiment\
  │        ├─ vader_lexicon.xml
  │        └─ vader_lexicon.zip
  ├─ src\
  │  ├─ getcontent.py
  │  ├─ getsentiment.py
  │  ├─ loader.py
  │  ├─ mongoconnect.py
  │  └─ scraper.py
  ├─ main.py
  ├─ requirements.txt
  ├─ README.md
  └─ LICENSE
```
## Prerequisites

To run the BBC Scraper locally, you need to have the following prerequisites installed:

- Python 3.9/3.10
- pip (Python package installer)
- MongoDB (Local install)

## Getting Started

To get started with the BBC Scraper, follow these steps:

1. Clone this repository to your local machine using the following command:
    ```bash
    $ git clone git@github.com:sarbhanub/bbc-scraper.git
    ```
2. Navigate to the project directory:
    ```bash
    $ cd bbc-scraper
    ```
3. Install the required Python dependencies:
    ```bash
    $ pip install -r requirements.txt
    ```
4. Run the scraper locally:
    ```bash
    $ python main.py
    ```

This will fetch articles present in the RSS feeds from BBC and will save it to MongoDB if you're running it locally on port 27017 (default).

## GitHub Actions

The scraper is integrated with GitHub Actions, allowing you to automate the scraping process and schedule it to run multiple times a day and save it directly to a MongoAtlas cluster running on cloud. The workflow file can be found in the .github/workflows directory.

The default configuration is set to run the scraper every 3 hours (8 times a day). You can modify the schedule by editing the .github/workflows/actions.yml file.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.

## Disclaimer

Please note that scraping websites may be subject to legal restrictions or terms of service. Make sure to review and comply with any applicable terms and conditions when using this scraper. BBC Scraper is provided as-is and the developers are not responsible for any misuse or legal consequences resulting from its use.
