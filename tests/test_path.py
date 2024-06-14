

import sys
import os
sys.path.append(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
from src.start.generate_universe import generate_universe

print(generate_universe((10, 10)))
