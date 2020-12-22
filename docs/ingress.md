# cnvrg stack - ingress
One of the required components of cnvrg stack is K8S ingress controller.
cnvrg control plan support the following controllers 
1. Istio Ingress Controller (default ingress, shipped by default with each cnvrg deployment ) 
2. Nginx Ingress Controller 
3. OpenShift Router
4. NodePort (in setups where ingress controller is not an option)

### Istio on-prem deployments `kube-proxy` with proxy mode `iptables`,
In case of on-prem deployments with  
cnvrg stack will create ingress service with [externalsIps](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips) 
The `externalsIps` list should include one or more (might be even all) nodes IPs.

### Istio on-prem deployments `kube-proxy` with proxy mode `ipvs`,
In case of on-prem deployments with  
cnvrg stack will create ingress service with [externalsIps](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips)
The `externalsIps` list *should not have any cluster node IPs*, 
but allocate one or more free IPs from your subnet. 

## Change the `kube-proxy` proxy mode (kubeadm tested scenario)
To change `kube-proxy` proxy mode run the following commands 
1. Edit `kube-proxy` configmap in `kube-system` namespace  
```bash
kubectl edit cm kube-proxy -nkube-system
```
2. Change `mode` to either `ipvs` or `iptables`
```yaml
apiVersion: v1
data:
  config.conf: |-
    apiVersion: kubeproxy.config.k8s.io/v1alpha1
    ...
    mode: ipvs
    ...
```

## kubeadm cluster setup - configure `kube-proxy` proxy mode
Use the following configuration to use either `ipvs` or `iptables` for `kubeadm` based clusters
```yaml
---
apiVersion: kubeproxy.config.k8s.io/v1alpha1
kind: KubeProxyConfiguration
mode: ipvs #iptables
```