import yaml
import inflection
from pandas.io.json._normalize import nested_to_record


def get_section_name(vars_path):
    if '/' in vars_path:
        return inflection.camelize(vars_path.split("/")[1], False)
    else:
        return inflection.camelize(vars_path, False)


def parse_roles_vars():
    helm_params = {}
    with open(r'../playbooks/cnvrg.yml') as file:
        playbook = yaml.load(file, Loader=yaml.FullLoader)

    for task in playbook[0]['tasks']:
        if 'name' not in task:
            continue
        if task['name'] == 'Include vars':
            for vars_path in task['with_items']:
                if vars_path == "vars/globals.yml":
                    vars_path = f"../playbooks/{vars_path}"
                with open(vars_path) as f:
                    nested_vars = yaml.load(f, Loader=yaml.FullLoader)
                    flat = nested_to_record(nested_vars, sep='.')
                    for key, value in flat.items():
                        if isinstance(value, str) and '{{' in value:
                            continue
                        param_name = inflection.camelize(key, False)
                        helm_params[param_name] = value
    return helm_params


def get_docs_header():
    return """
### Chart options 
|**key**|**default value**|**description**\n| ---|---|---|
|`createNs`| true | set to `false` if cnvrg namespaces already exists 
|`specProfile`| default | can be on of the following `default` `microk8s`
|`computeProfile`| default |can be on of the following `default` `micro`
|`storageProfile`| default | can be on of the following `default` `micro`
"""


def parse_docs(helm_params):
    params_dump_docs = get_docs_header()
    for param_name, param_value in helm_params.items():
        if "descriptions" in param_name:
            continue
        if param_value == "":
            param_value = "-"
        description = get_param_desc(param_name, helm_params)
        params_dump_docs += f"|`{param_name}`|{param_value}|{description}\n"

    with open("docs_tmpl", mode="r") as f:
        content = f.read()
        content = content.replace("__DUMP__ALL__PARAMS_HERE__", params_dump_docs)

    with open("../README.md", "w") as f:
        f.write(content)


def get_param_desc(param_name, helm_params):
    param = param_name.split(".")
    # global param, description configured at global section
    if len(param) < 1:
        # Bad param . . .
        return ""
    if len(param) == 0:
        description_key = f"descriptions.{param_name}"
    else:
        description_key = f"{param[0]}.descriptions.{param_name}"
    if description_key in helm_params:
        return helm_params[description_key].replace("\n", "")
    return ""


def insert(dct, lst):
    for x in lst[:-2]:
        dct[x] = dct = dct.get(x, dict())
    dct.update({lst[-2]: lst[-1]})


def convert_nested(dct):
    # empty dict to store the result
    result = dict()
    # create an iterator of lists
    # representing nested or hierarchial flow
    lsts = ([*k.split("."), v] for k, v in dct.items())
    # insert each list into the result
    for lst in lsts:
        insert(result, lst)
    return result


def dump_chart_values(helm_params):
    res_dict = {}
    # Build helm values
    for k, v in convert_nested(helm_params).items():
        if "descriptions" in k:
            continue
        res_dict[k] = v
    return res_dict


def save_chart_values(chart_values):
    # Dump yaml
    print(yaml.dump(chart_values, default_flow_style=False, sort_keys=False, width=float("inf")))
    # with open("../chart/values.yaml", "w") as f:
    #     f.write(yaml.dump(chart_values, default_flow_style=False, sort_keys=False, width=float("inf")))


def dump_cnvrg_app_instance(chart_values):
    with open("instance_tmpl.yaml", mode="r") as f:
        content = f.read()
        content = yaml.load(content, Loader=yaml.FullLoader)
        content['spec'] = chart_values
    print(yaml.dump(content, default_flow_style=False, sort_keys=False, width=float("inf")))
    # with open("../chart/templates/cnvrg-app.yaml", "w") as f:
    #     f.write(yaml.dump(content, default_flow_style=False, sort_keys=False, width=float("inf")))


def camelize_keys(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from camelize_keys(value)
        else:
            camelized_key = inflection.camelize(key, False)
            yield (key, camelized_key)


def filter_helm_params(helm_params, default_v=None):
    res = {}
    for k, v in helm_params.items():
        if "descriptions" in k:
            continue
        if default_v is None:
            res[k] = v
        else:
            value = "{{ .Values." + k + " }}"
            res[k] = value
    return res


def replace_quotes():
    with open("../chart/values.yaml", "r+") as f:
        content = f.read()
        f.seek(0)
        content = content.replace("'", '"')
        f.write(content)
        f.truncate()

    with open("../chart/templates/cnvrg-app.yaml", "r+") as f:
        content = f.read()
        f.seek(0)
        content = content.replace("'", '"')
        f.write(content)
        f.truncate()


def main():
    # Pars docs
    helm_params = parse_roles_vars()
    parse_docs(helm_params)

    # dump chart values
    # filtered_helm_values = filter_helm_params(helm_params)
    # helm_values = dump_chart_values(filtered_helm_values)
    # save_chart_values(helm_values)

    # dump cnvrg object
    # filtered_helm_values = filter_helm_params(helm_params, True)
    # cnvrg_object = dump_chart_values(filtered_helm_values)
    # dump_cnvrg_app_instance(cnvrg_object)

    # WTF?!
    # replace_quotes()


if __name__ == "__main__":
    main()
