import sys
import os
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from common.const import PAGINATION

def main() -> int:
    print("Hello")
    print(BASE_PATH)
    print(PAGINATION)
    return 0

if __name__ == '__main__':
    main()
    sys.exit(0)