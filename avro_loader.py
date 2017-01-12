import argparse
import avro
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from pprint import pprint


def load_and_print(filename):
    schema = avro.schema.parse(open(filename).read())
    pprint(schema.to_json())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(u'--filename', help=u'The name, including path, of the Avro schema to load.')
    args = parser.parse_args()

    if not args.filename:
        raise Exception(u'No filename')

    filename = args.filename
    load_and_print(filename)
