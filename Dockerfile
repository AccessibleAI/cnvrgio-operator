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
USER 0
RUN yum install wget openssl -y
RUN export VERSION=$(curl --silent "https://api.github.com/repos/cloudflare/cfssl/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/') \
    && export VNUMBER=${VERSION#"v"} \
    && wget https://github.com/cloudflare/cfssl/releases/download/${VERSION}/cfssl_${VNUMBER}_linux_amd64 -O cfssl \
    && chmod +x cfssl && mv cfssl /usr/local/bin \
    && wget https://github.com/cloudflare/cfssl/releases/download/${VERSION}/cfssljson_${VNUMBER}_linux_amd64 -O cfssljson \
    && chmod +x cfssljson && mv cfssljson /usr/local/bin
USER ${USER_UID}
COPY watches.yaml ${HOME}/watches.yaml
COPY roles/ ${HOME}/roles/
COPY playbooks/ ${HOME}/playbooks/
