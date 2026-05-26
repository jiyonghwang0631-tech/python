# python3.10 -m pip install pyyaml

from pathlib import Path

import yaml


def main():
    path = Path(r"/home/korea_hrd_1_2/python/Python_example/basic/data/test.json")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
        print(data["abc"])
        print(data["subject"]["korean"])


if __name__ == "__main__":
    main()