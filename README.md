# busca-querido-diario
Project to enable search of key words in text files extracted by the [Querido Diário](https://github.com/okfn-brasil/diario-oficial).

## Dependencies
- [Python3](https://www.python.org/)
- [Elasticsearch](https://www.elastic.co/)

## Setup
`pip install -r requirements.txt`

### Install Elasticsearch on Ubuntu 18.04
Elasticsearch required Java to run on any system. Make sure your system has Java installed by running following command.
`java -version`

The Elasticsearch official team provides an apt repository to install Elasticsearch on Ubuntu Linux system.
```
sudo apt-get install apt-transport-https
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
add-apt-repository "deb https://artifacts.elastic.co/packages/7.x/apt stable main"
sudo apt-get update
sudo apt-get install elasticsearch
```
To configure Elasticsearch to start automatically when the system boots up, run the following commands:

`sudo /bin/systemctl enable elasticsearch.service`

Elasticsearch can be started and stopped as follows:
```
sudo systemctl start elasticsearch.service
sudo systemctl stop elasticsearch.service
```
If you do not want to install ElasticSearch in your local machine you can run it in a container with one of the
following commands:

```bash
# These commands are NOT recommended for production. 
$ docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.7.1
# or
$ podman run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.7.1
```

## Run
From the output of the [Querido Diário](https://github.com/okfn-brasil/diario-oficial), it is possible to access files in text format of the Brazilian municipal gazettes. for example:
`scrapy crawl sc_florianopolis -a start_date='2020-05-05'`

The above command collects all the diaries of Florianópolis city, as of the date 2020-05-05.

With the text files obtained using the scraper, it is necessary to point out where the files are for the collection of information made by elasticsearch:
`python load_data.py /home/user/path-to/diario-oficial/data/full/`

**Finally, here is the command to search for a word**:
`python search.py covid-19`

The result is a folder named with the word used in the search: `covid-19/*`
