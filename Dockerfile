FROM quay.io/operator-framework/ansible-operator:v1.4.0

LABEL name="cnvrg-operator" \
	  vendor="cnvrg.io" \
      version="v1.0" \
      release="v1.0" \
 	  summary="cnvrg.io Operator" \
      description="cnvrg.io Operator"

COPY license /licenses
COPY requirements.yml ${HOME}/requirements.yml
RUN ansible-galaxy collection install -r ${HOME}/requirements.yml \
 && chmod -R ug+rwx ${HOME}/.ansible
USER 0
RUN yum install openssl -y \
    && export VERSION=$(curl --silent "https://api.github.com/repos/cloudflare/cfssl/releases/latest" | grep '"tag_name"' | sed -E 's/.*"([^"]+)".*/\1/') \
    && export VNUMBER=${VERSION#"v"} \
    && curl -sLo /usr/local/bin/cfssl https://github.com/cloudflare/cfssl/releases/download/${VERSION}/cfssl_${VNUMBER}_linux_amd64  \
    && curl -sLo /usr/local/bin/cfssljson https://github.com/cloudflare/cfssl/releases/download/${VERSION}/cfssljson_${VNUMBER}_linux_amd64 \
    && curl -sLo /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.18.8/bin/linux/amd64/kubectl \
    && curl -sLo /usr/local/bin/jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 \
    && chmod +x /usr/local/bin/cfssl \
    && chmod +x /usr/local/bin/cfssljson \
    && chmod +x /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/jq
USER ${USER_UID}
COPY watches.yaml ${HOME}/watches.yaml
COPY roles/ ${HOME}/roles/
COPY playbooks/ ${HOME}/playbooks/
