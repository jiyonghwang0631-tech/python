import json
from pathlib import Path

def main():
    path = Path(r"/home/korea_hrd_1_2/python/Python_example/basic/data/test.json")
    
    with path.open("r", encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        print(type(data))

if __name__ == "__main__":
    main()
