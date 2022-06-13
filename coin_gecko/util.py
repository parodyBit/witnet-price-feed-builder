from typing import Any, List, Dict, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser

import csv
import json
import os


def save_json_file(file_name: str, data: dict):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def save_csv_file(file_name: str, lines: list):
    with open(file_name, mode='w', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for line in lines:
            file_writer.writerow(line)
        csv_file.close()


def load_csv_file(file_name: str):
    lines = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            lines.append(row)
            if line_count == 0:
                line_count += 1
            else:
                line_count += 1
        print(f'Loaded file {file_name} containing {line_count} lines.')
    return lines


def load_json_file(file_name: str) -> map:
    f = open(file_name, encoding='utf8')
    # returns JSON object as
    # a dictionary
    return json.load(f,)


def file_exists(file_name: str) -> bool:
    if os.path.isfile(file_name):
        print("File exists")
        return True
    return False


def compare_json_files(old_json, new_json):

    mismatch = False
    new_items = {}
    for item in new_json:
        if item not in old_json:
            print(f'New Item: [{item}] needs to be synced to database.')
            new_items[item] = new_json[item]
            mismatch = True


T = TypeVar("T")


def from_none(x: Any) -> Any:
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    # assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x
