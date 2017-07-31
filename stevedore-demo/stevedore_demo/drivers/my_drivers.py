import argparse

from stevedore import driver


class SimpleDriver(object):
    DATA = {
        'ex': 'EX',
        'b': 'B',
        'long': 'example ' * 40
    }

    def __init__(self):
        parser = self.get_parser()
        self.manager = driver.DriverManager(
            namespace='mydrivers',
            name=parser.format,
            invoke_on_load=True,
            invoke_args=(parser.width,),
        )

    def run_driver(self):
        for chunk in self.manager.driver.format(self.DATA):
            print(chunk, end='')

    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'format',
            nargs='?',
            default='simple',
            help='output format to print'
        )
        parser.add_argument(
            '--width',
            default=30,
            type=int,
            help='Maximum output width for text'
        )
        return parser.parse_args()

if __name__ == "__main__":
    demo = SimpleDriver()
    demo.run_driver()
