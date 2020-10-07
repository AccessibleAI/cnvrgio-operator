FROM python:3.8.6
WORKDIR /root
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.18.8/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl
RUN curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
CMD python tests/run_tests.py