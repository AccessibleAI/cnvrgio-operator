import yaml
import inflection
from pandas.io.json._normalize import nested_to_record


def parse_roles_vars():
    docker_images = {}
    with open('../chart/values.yaml') as f:
        nested_vars = yaml.load(f, Loader=yaml.FullLoader)
        flat = nested_to_record(nested_vars, sep='.')
        for key, value in flat.items():
            if isinstance(value, str) and ('image' in key.lower()):
                if 'istio.proxyImage' in key or 'istio.mixerImage' in key or 'istio.pilotImage' in key:
                    value = 'docker.io/istio/' + value
                if 'docker' not in value:
                    value = 'docker.io/' + value
                docker_images[key] = value

    return docker_images


def helm_command_offline(images_dict):
    helm_command = {}
    for key, value in images_dict.items():
        value = value.split('/')[-2:]
        if 'docker.io' in value[0]:
            value.pop(0)
        value = "offline_repo/" + '/'.join(value)
        key = f"--set {key}"
        helm_command[key] = value + ' \\'
    return helm_command


def parse_docs(images, helm_params):
    params_dump_docs = ""
    for key, value in images.items():
        params_dump_docs += f"{value}\n"

    helm_params_dump_docs = ""
    for key, value in helm_params.items():
        helm_params_dump_docs += f"{key} {value}\n"

    with open("docs_images_tmpl", mode="r") as f:
        content = f.read()
        content = content.replace("__DUMP_IMAGES__", params_dump_docs)
        content = content.replace("__DUMP_IMAGES_COMMANDS__", helm_params_dump_docs)

    with open("../docs/offline_images.md", "w") as f:
        f.write(content)


def main():
    images = parse_roles_vars()
    helm_command = helm_command_offline(images)
    parse_docs(images, helm_command)


if __name__ == "__main__":
    main()
