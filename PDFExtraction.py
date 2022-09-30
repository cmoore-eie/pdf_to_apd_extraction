import configparser
import getopt
import sys

import PDFProcessor

version_number = '0.3'
process_errors = dict()
help_str = '''

Please supply the arguments for -c
        -c, --config - path to the json configuration file
        -h, --help - displays this text

        '''

def print_logo():
    print('                     __,__')
    print('            .--.  .-"     "-.  .--.')
    print("           / .. \/  .-. .-.  \/ .. \ ")
    print("          | |  '|  /   Y   \  |'  | |")
    print('          | \   \  \ 0 | 0 /  /   / |')
    print("           \ '- ,\.-'`` ``'-./, -' /")
    print("            `'-' /_   ^ ^   _\ '-'`")
    print('                |  \._   _./  |')
    print('                \   \ `~` /   /')
    print("                 '._ '-=-' _.'")
    print("                    '~---~'")
    print(" __      ___           __  __          _            ")
    print(" \ \    / (_)___ ___  |  \/  |___ _ _ | |_____ _  _ ")
    print("  \ \/\/ /| (_-</ -_) | |\/| / _ \ ' \| / / -_) || |")
    print("   \_/\_/ |_/__/\___| |_|  |_\___/_||_|_\_\___|\_, |")
    print("                                               |__/ ")
    print(f"                  Version - {version_number}")




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
            file = open(config_file)
        except FileNotFoundError:
            print(f'ERROR - The configuration file {config_file} has not been found')
            sys.exit(1)

        config = configparser.ConfigParser()
        config.read('sample_config.txt')
        config_dict = {s: dict(config.items(s)) for s in config.sections()}
        PDFProcessor.process(config_dict)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(help_str)
        sys.exit()
    main(sys.argv[1:])
