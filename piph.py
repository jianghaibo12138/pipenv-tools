#!/usr/bin/python

import os
from optparse import OptionParser

PIPENV_FILE_NAME = "Pipfile"
PIPENV_FILE_COPY_NAME = "tmp"

PIPENV_FILE_PATH = os.path.join(os.getcwd(), PIPENV_FILE_NAME)
PIPENV_FILE_COPY_PATH = os.path.join(os.getcwd(), PIPENV_FILE_COPY_NAME)

AIM_REPO_URL = "https://pypi.tuna.tsinghua.edu.cn/simple"


def rewrite():
    with open(PIPENV_FILE_PATH, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            line = line.strip()
            if line.startswith("url"):
                lis = line.split("=")
                lis[1] = '= "{}"\n'.format(AIM_REPO_URL)
                lines[index] = "".join(lis)
        with open(PIPENV_FILE_COPY_PATH, "w") as fb:
            fb.writelines(lines)


def replace():
    if os.path.isfile(PIPENV_FILE_PATH):
        if os.path.isfile(PIPENV_FILE_COPY_PATH):
            try:
                os.rename(PIPENV_FILE_NAME, ".{}_back".format(PIPENV_FILE_COPY_NAME))
                os.rename(PIPENV_FILE_COPY_NAME, PIPENV_FILE_NAME)
                os.remove(".{}_back".format(PIPENV_FILE_COPY_NAME))
            except Exception as e:
                raise e


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-r", "--registry", dest="registry", help="The registry you changed to.")
    options, _ = parser.parse_args()
    AIM_REPO_URL = options.registry if options.registry else AIM_REPO_URL
    rewrite()
    replace()
