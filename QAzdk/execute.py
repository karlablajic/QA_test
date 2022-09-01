import os

import pytest as pytest
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--version_browser", default="desktop")
args = parser.parse_args()
version = args.version_browser
os.environ["version_browser"] = version

if version == "mobile":
    pytest.main(
        ["test_cases_mobile.py"]
    )
else:
    pytest.main(
        ["test_cases.py"]
    )
