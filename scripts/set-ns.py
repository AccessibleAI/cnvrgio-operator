#!/usr/local/bin/python3
import sys
import glob


def main():
    if len(sys.argv) < 2:
        print("error: missing source dir. Example: escape-ansible-var.py /tmp/manifests namespace: xyz")
        exit(1)

    src_dir = sys.argv[1]
    ns = sys.argv[2]
    print(ns)
    for file in glob.glob(f"{src_dir}/*.yaml"):
        print(file)
        with open(file=file, mode="r+") as f:
            content = f.read()
            f.seek(0)
            content = content.replace(ns, 'namespace: "{{meta.namespace}}"')
            f.write(content)
            f.truncate()


if __name__ == "__main__":
    main()
