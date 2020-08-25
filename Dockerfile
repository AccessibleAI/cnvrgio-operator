FROM quay.io/operator-framework/ansible-operator:v1.0.0

LABEL name="cnvrg-operator" \
	  vendor="cnvrg.io" \
      version="v0.350.0" \
      release="v0.350.0" \
 	  summary="cnvrg.io Operator" \
      description="cnvrg.io Operator"

COPY license /licenses
COPY requirements.yml ${HOME}/requirements.yml
RUN ansible-galaxy collection install -r ${HOME}/requirements.yml \
 && chmod -R ug+rwx ${HOME}/.ansible

COPY watches.yaml ${HOME}/watches.yaml
COPY roles/ ${HOME}/roles/
COPY playbooks/ ${HOME}/playbooks/
