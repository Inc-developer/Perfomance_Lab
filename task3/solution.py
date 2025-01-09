import sys
import json


def load_info(file):
    with open(file, "r") as file_data:
        values = json.load(file_data)
    return values

def dump_info(info, report_file):
    with open(report_file, "w+") as file:
        json.dump(info, file, indent=2)


def make_report(values, tests):
    if type(tests) == type(dict()):
        for _ in tests.values():
                for i in _:
                    if i.get("values"):
                        for first_level in values.values():
                            for val in first_level:
                                if i["id"] == val["id"]:
                                    i["value"] = val["value"]
                        make_report(values, i.get("values"))
                    else:
                        for first_level in values.values():
                            for val in first_level:
                                if i["id"] == val["id"]:
                                    i["value"] = val["value"]
    if type(tests) == type(list()):
            for i in tests:
                print(i)
                if i.get("values"):
                    for first_level in values.values():
                            for val in first_level:
                                if i["id"] == val["id"]:
                                    i["value"] = val["value"]
                    make_report(values, i.get("values"))
                else:
                    for first_level in values.values():
                        for val in first_level:
                            if i["id"] == val["id"]:
                                i["value"] = val["value"]


if __name__ == "__main__":
    if len(sys.argv) == 4:
        values, tests = load_info(sys.argv[1]), load_info( sys.argv[2])
        make_report(values, tests)
        dump_info(tests, sys.argv[3])
    else:
        print("Need 3 args (file path's)")