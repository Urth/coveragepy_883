import subprocess
from unittest import TestCase


class CommandTestCase(TestCase):
    def test_command(self):
        output = subprocess.check_output(['python', 'command.py'])
        self.assertEqual(output, b'Hello World!\n')
