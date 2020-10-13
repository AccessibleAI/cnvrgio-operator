FROM python:3.8.6
WORKDIR /root
RUN apt update -y && \
     apt-get install -y \
     gettext-base \
     jq
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.18.8/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl
RUN curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh
CMD python tests/run_tests.py