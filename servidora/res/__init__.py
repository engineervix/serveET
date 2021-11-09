# Read in yaml as dictionary
from pathlib import Path

from util import parser

STRINGS = parser.parse_yaml(f"{Path(__file__).parent}/strings.yml")
