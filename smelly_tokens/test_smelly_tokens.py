# coding: utf-8

import os
import fnmatch
import pkgutil
from token import NAME
from tokenize import generate_tokens

from django.test import TestCase
from django.conf import settings


PY_FILE_EXTENSION = '*.py'

NO_QUALITY_CHECK_LINE_MARK = '# noqa'
NO_QUALITY_CHECK_FILE_MARK = '# smelly_tokens: noqa'


class SmellyTokensTestCase(object):
    _token = ''

    def test_check_token_exists(self):
        errors = []
        for module in getattr(settings, 'SMELLY_TOKENS_APPLICATIONS', []):
            module_dir = pkgutil.get_loader(module).filename
            for directory, _, files in os.walk(module_dir):
                if directory in getattr(
                        settings, 'SMELLY_TOKENS_EXCLUDE_DIRS', []):
                    continue
                for file in fnmatch.filter(files, PY_FILE_EXTENSION):
                    f = open(os.path.join(directory, file))
                    for kind, token, start, _, whole in \
                            generate_tokens(f.readline):
                        if whole.startswith(NO_QUALITY_CHECK_FILE_MARK):
                            break
                        if whole.strip().endswith(NO_QUALITY_CHECK_LINE_MARK):
                            continue
                        if kind != NAME:
                            continue
                        if token == self._token:
                            errors.append("'{}' left at '{}', line {}".format(
                                token, file, start[0]))
                    f.close()

        self.assertTrue(len(errors) == 0, '\n'.join(errors))


class EvalTokenTestCase(SmellyTokensTestCase, TestCase):
    _token = 'eval'


class PdbTokenTestCase(SmellyTokensTestCase, TestCase):
    _token = 'pdb'


class PrintTokenTestCase(SmellyTokensTestCase, TestCase):
    _token = 'print'
