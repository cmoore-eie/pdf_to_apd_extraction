import configparser
import getopt
import sys

import config
import pdf_processor
from utility import wise_monkey_says, load_shape_files

version_number = '0.3'
process_errors = dict()
help_str = '''

Please supply the arguments for -c
        -c, --config - path to the json configuration file
        -h, --help - displays this text

        '''


def print_logo():
    f = open('logo.txt', 'r')
    print(''.join([line for line in f]))
    print(f"Version - {version_number}")


def main(argv):
    print("")
    print_logo()
    print("")
    config_file: str = ''

    try:
        opts, args = getopt.getopt(argv, 'c:', ['help', 'config ='])
        for opt, arg in opts:
            if opt in ['-c', '--config']:
                config_file = arg.strip()
            elif opt in ['-h', '--help']:
                print(help_str)
                sys.exit()
            else:
                sys.exit()
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)

    if config_file == '':
        process_errors[len(process_errors) +
                       1] = "-c (--config) missing and is required"
        sys.exit(1)

    if len(process_errors) > 0:
        print("")
        print("Missing Parameter Information")
        print("=============================")
        for error_item in process_errors:
            print(f"({error_item}) : {process_errors[error_item]}")
    else:
        try:
            conf = configparser.ConfigParser()
            conf.read(config_file)
            config.config_dict = {s: dict(conf.items(s)) for s in conf.sections()}
            if 'json_store_location' in config.config_dict['Base Information'].keys():
                config.json_store_location = config.config_dict['Base Information']['json_store_location']
                load_shape_files()
            else:
                wise_monkey_says('You forgot to tell me where the json files can be found')
                wise_monkey_says('if you set the json_store in the configuration file we can try again')
                sys.exit(1)
            pdf_processor.process()
        except OSError:
            print(f'ERROR - The configuration file {config_file} has not been found')
            sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(help_str)
        sys.exit()
    main(sys.argv[1:])
