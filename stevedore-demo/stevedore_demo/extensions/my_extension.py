import argparse

from stevedore import extension

class SimpleExtension(object):
    DATA = {
        'ex': 'EX',
        'b': 'B',
        'long': 'example ' * 40
    }

    def __init__(self):
        parser = self.get_parser()
        self.manager = extension.ExtensionManager(
            namespace='myextensions',
            invoke_on_load=True,
            invoke_args=(parser.width,),
        )

    def format_data(self, ext, data):
        return (ext.name, ext.obj.format(data))

    def run_extension(self):
        results = self.manager.map(self.format_data, self.DATA)
        for name, result in results:
            print('Formatter: {0}'.format(name))
            for chunk in result:
                print(chunk, end='')
            print('')

    def get_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--width',
            default=30,
            type=int,
            help='Maximum output width for text'
        )
        return parser.parse_args()

if __name__ == "__main__":
    ext = SimpleExtension()
    ext.run_extension()