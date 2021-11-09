from pathlib import Path

from . import parser

CONFIG = parser.parse_yaml(f"{Path(__file__).parent.parent}/config.yml")
