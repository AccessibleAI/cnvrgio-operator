#!/usr/local/bin/python3
import sys


def find_unique_char(content):
    unique_chars = ["@", "~", "%", "^", "~"]
    for uc in unique_chars:
        if content.find(uc) == -1:
            return uc
    print("error: can't find unique chart, try add some unique_chars")
    exit(1)


def main():
    if len(sys.argv) < 2:
        print("error: missing file path, example: escape-ansible-var.py file.yaml")
        exit(1)

    file_path = sys.argv[1]
    with open(file=file_path, mode="r+") as f:
        content = f.read()
        f.seek(0)
        uc = find_unique_char(content)
        replace = "{{ " + "'" + "{{" + "' " + uc
        content = content.replace("{{", replace)
        content = content.replace("}}", "{{ '}}' }}")
        content = content.replace(uc, "}}")
        f.write(content)
        f.truncate()


if __name__ == "__main__":
    main()
