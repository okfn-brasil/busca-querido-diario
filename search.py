import json
import os
import sys

import elasticsearch

INDEX_NAME = 'consultas'


def get_word():
    """
    Retorn a query string passed as a command line argument.
    """
    return ' '.join(sys.argv[1:])

def create_output_path():
    path = get_word()
    try:
        os.mkdir(path)
    except OSError:
        print ("directory %s already exists failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def main():
    word = get_word()
    create_output_path()

    es = elasticsearch.Elasticsearch(hosts=['localhost'])
    query = {
        'query': {'query_string': {'query': word, 'default_field': 'text'}}
    }
    result = es.search(index=INDEX_NAME, body=query)

    for hit in result['hits']['hits']:
        gazette = hit['_source']['text']

        with open('{}/{}.txt'.format(get_word(), hit['_source']['id']), 'w') as file:
            file.write(gazette)


if __name__ == '__main__':
    main()