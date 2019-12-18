import sys
from datetime import datetime
import argparse


def create_log(name):
    if len(name) > 0:
        with open(name, "w", encoding="utf-8") as f:
            pass


def write_log(name, text):
    if text is not None:
        with open(name, "a", encoding="utf-8") as f:
            f.write("{} {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text))


def create_parser():
    parser = argparse.ArgumentParser(description="main.py [-log <log_name>] "
                                                 "[-timestamp] "
                                                 "[-digits <number_of_digits>] "
                                                 "-full_match <symb>"
                                                 "-partial_match <symb>")
    parser.add_argument("-log", type=str, default="logfile.log", help="Имя файла лога. По умолчанию logfile.log")
    parser.add_argument("-timestamp", type=str, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), help="Метка времени (когда запустили скрипт)")
    parser.add_argument("-digits", type=int, default=3, choices=[3, 4, 5], help="Число цифр в числе. По умолчанию 3")
    parser.add_argument("-full_match", type=str, default='V', help="Буква при полном совпадении. По умолчанию V")
    parser.add_argument("-partial_match", type=str, default='K', help="Буква при неполном совпадении. По умолчанию K")

    return parser


def main():
    # args = sys.argv[1:]
    # log_text = f"Тип аргументов: {type(args)}, список аргументов: {args}"
    # print(log_text)
    # if "-log" in args:
    #     filename = args[args.index("-log") + 1]
    #     # print(f"Имя файла из параметров: {filename}")
    #     create_log(filename)
    #     write_log(filename, log_text)

    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    log_text = f"Тип аргументов: {type(args)}, список аргументов: {args}"
    print(log_text)
    args_dict = vars(args)
    log_text = f"Тип аргументов: {type(args_dict)}, список аргументов: {args_dict}"
    filename = args.log
    create_log(filename)
    write_log(filename, log_text)


if __name__ == "__main__":
    main()