import logging

from utils.miscellaneous.create_files import create_files
from data import config
from data.models import ProgramAction
from functions.find import find
from functions.parse import parse

if __name__ == '__main__':
    print(f'\nSoftware version: {config.GREEN}{config.VERSION}{config.RESET_ALL}\n')
    create_files()
    while True:
        action = None
        print('''Select the action:
1) Parse eligible addresses.
2) Find eligible addresses.
3) Exit.''')
        try:
            action = int(input('> '))
            print()
            if action == ProgramAction.Parse:
                parse()

            elif action == ProgramAction.Find:
                find()

            else:
                break

        except KeyboardInterrupt:
            print()

        except ValueError:
            print(f"{config.RED}You didn't enter a number!{config.RESET_ALL}")

        except BaseException as e:
            logging.exception('main')
            print(f'\n{config.RED}Something went wrong: {e}{config.RESET_ALL}\n')

        if action:
            input(f'\nPress {config.LIGHTGREEN_EX}Enter{config.RESET_ALL} to exit.\n')
            break
