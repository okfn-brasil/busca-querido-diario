# busca-querido-diario
Project to enable search of key words in text files extracted by the [Querido Diário](https://github.com/okfn-brasil/diario-oficial).

## Dependencies
- [Python3](https://www.python.org/)
- [Elasticsearch](https://www.elastic.co/)

## Setup
`pip install -r requirements.txt`

## Run
From the output of the [Querido Diário](https://github.com/okfn-brasil/diario-oficial), it is possible to access files in text format of the Brazilian municipal gazettes. for example:
`scrapy crawl sc_florianopolis -a start_date='2020-05-05'`

The above command collects all the diaries of Florianópolis city, as of the date 2020-05-05.

With the text files obtained using the scraper, it is necessary to point out where the files are for the collection of information made by elasticsearch:
`python load_data.py /home/user/path-to/diario-oficial/data/full/`

**Finally, here is the command to search for a word**:
`python search.py covid-19`

The result is a folder named with the word used in the search: `covid-19/*`
