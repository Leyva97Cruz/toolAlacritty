import argparse

class ArgsCli:

    __parser = ""

    def Cli(self):

        self.__parser = argparse.ArgumentParser(

            prog= 'Pycolor',
            description= 'command line for changes themes or colors in the terminal alacritti',
        )

        self.__parser.add_argument(
            '-t',
            '--theme',
            help= 'Name of the Teme'
        )

        self.__parser.add_argument(
            '-f',
            '--font',
            help= 'Name of the Font'
        )
        return self.__parser.parse_args()