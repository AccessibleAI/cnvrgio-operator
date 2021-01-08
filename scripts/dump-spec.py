import yaml
import glob
import json


def parse_roles_vars():
    spec = {'cnvrgApp': {}}
    vars_files = glob.glob('../roles/*/vars/main.yml')
    vars_files.append('../playbooks/vars/globals.yml')

    for var_file in vars_files:
        with open(var_file) as f:
            nested_vars = yaml.load(f, Loader=yaml.FullLoader)
            if nested_vars is None:
                continue
            spec['cnvrgApp'] = {**spec['cnvrgApp'], **nested_vars}
    return spec


def main():
    # get operator spec
    spec = parse_roles_vars()
    print(json.dumps(spec))


if __name__ == "__main__":
    main()
