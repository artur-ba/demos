import logging

from cliff.command import Command
from cliff.hooks import CommandHook


class Hooked(Command):
    """Sample command to demonstrate how the hooks works."""
    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.app.stdout.write('This command is an extension\n')


class Hook(CommandHook):
    """Sample for the 'hooked' command."""
    def get_parser(self, parser):
        print('sample hook with get_parser')
        parser.add_argument('--added-by-hook-cmd')
        return parser

    def get_epilog(self):
        return 'extension epilog text'

    def before(self, parsed_args):
        self.cmd.app.stdout.write('before\n')

    def after(self, parsed_args, return_code):
        self.cmd.app.stdout.write('after\n')
