from datetime import datetime
import glob
import sys

import elasticsearch


INDEX_NAME = 'consultas'

def get_path():
    """
    Retorn a query string passed as a command line argument.
    """

    return ' '.join(sys.argv[1:])


def create_es_index(es):
    try:
        es.indices.delete(index=INDEX_NAME)
    except:
        print('Cannot delete index')
    es.indices.create(index=INDEX_NAME)


def load_data_into_es(es):
    path = get_path()
    gazette_list = glob.glob('{}*.txt'.format(path))

    for index, gazzete in enumerate(gazette_list):
        with open(gazzete) as file:
            data = file.read()
            ret = es.index(
                index=INDEX_NAME,
                id=index,
                body={
                    'id': index,
                    'text': data,
                },
            )


def query_es(es):
    """
    Search for a simple record to see if it is working.
    """
    print(es.get(index=INDEX_NAME, id=5)['_source'])


def main():
    es = elasticsearch.Elasticsearch(hosts=['localhost'])
    create_es_index(es)
    load_data_into_es(es)
    query_es(es)


if __name__ == '__main__':
    main()