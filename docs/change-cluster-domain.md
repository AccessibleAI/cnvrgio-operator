# cnvrg Cluster Domain change

Follow these steps to change your cnvrg cluster domain.

### Changing Cluster Domain in legacy deployments  (without cnvrg operator)

Perform the following actions to change cluster domain name
- Define your new cluster domain 
    ```bash
    export NEW_CLUSTER_DOMAIN=cnvrg.new.cluster.domain.example.com 
    ```
- Update following keys in `env-secret` K8S secret
    - `DEFAULT_COMPUTE_CLUSTER_DOMAIN`
    - `APP_DOMAIN`
    - `DEFAULT_URL`
    - `CNVRG_STORAGE_ENDPOINT`
    ```bash
    kubectl patch secret env-secrets -ncnvrg \
    --type='json' -p="[{'op' : 'replace' ,'path' : '/data/DEFAULT_COMPUTE_CLUSTER_DOMAIN' ,'value' : '$(printf $NEW_CLUSTER_DOMAIN | base64)'}]"
    
    
    kubectl patch secret env-secrets -ncnvrg  \
    --type='json' -p="[{'op' : 'replace' ,'path' : '/data/APP_DOMAIN' ,'value' : '$(printf app.$NEW_CLUSTER_DOMAIN | base64)'}]"
    
    
    kubectl patch secret env-secrets -ncnvrg  \
    --type='json' -p="[{'op' : 'replace' ,'path' : '/data/DEFAULT_URL' ,'value' : '$(printf http://app.$NEW_CLUSTER_DOMAIN | base64)'}]"
    
    
    kubectl patch secret env-secrets -ncnvrg  \
    --type='json' -p="[{'op' : 'replace' ,'path' : '/data/CNVRG_STORAGE_ENDPOINT' ,'value' : '$(printf http://minio.$NEW_CLUSTER_DOMAIN | base64)'}]"	
    ```
- Update Istio Virtual Services  
    ```bash
    # Set VS_LIST to the valid VS names in your cluster, for example: app minio prometheus elasticsearch elasticalerts grafana grafana routing-service
    VS_LIST="app minio prometheus elasticsearch elasticalerts grafana grafana routing-service"
    for vs_name in $VS_LIST; do
        kubectl patch vs $vs_name -ncnvrg \
          --type='json' -p="[{'op' : 'replace' ,'path' : '/spec/hosts/0' ,'value' : '$vs_name.$NEW_CLUSTER_DOMAIN'}]"
    done
  
    ```  

- Update cnvrg Istio Gateway for Istio based deployments
    ```bash 
    kubectl patch gw cnvrg-gateway -ncnvrg \
	--type='json' -p="[{'op' : 'replace' ,'path' : '/spec/servers/0/hosts/0' ,'value' : '*.$NEW_CLUSTER_DOMAIN'}]"
    ``` 

- Optionally to enable https update the following keys 
    - `DEFAULT_URL`
    - `CNVRG_STORAGE_ENDPOINT`
    - `DEFAULT_COMPUTE_CLUSTER_HTTPS`
    ```bash
    kubectl patch secret env-secrets -ncnvrg \
       --type='json' -p="[{'op' : 'replace' ,'path' : '/data/DEFAULT_URL' ,'value' : '$(printf https://app.$NEW_CLUSTER_DOMAIN | base64)'}]"
    
    kubectl patch secret env-secrets -ncnvrg \
      --type='json' -p="[{'op' : 'replace' ,'path' : '/data/CNVRG_STORAGE_ENDPOINT' ,'value' : '$(printf https://minio.$NEW_CLUSTER_DOMAIN | base64)'}]"
    
    kubectl patch secret env-secrets -ncnvrg  \
      --type='json' -p="[{'op' : 'replace' ,'path' : '/data/DEFAULT_COMPUTE_CLUSTER_HTTPS' ,'value' : '$(printf true | base64)'}]"
    ```
    - Optionally for AWS based deployments apply ELB annotation on Istio Ingress services
    ```bash
    # For AWS ELB, add the following annotations
    # service.beta.kubernetes.io/aws-load-balancer-ssl-cert: set:certificate:aws:acm:arn
    # service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp
    # service.beta.kubernetes.io/aws-load-balancer-ssl-ports: https
    
    export ACM_ARN=aws:acm:arn
    kubectl patch svc istio-ingressgateway -ncnvrg \
      -p '{"metadata": {"annotations": {"service.beta.kubernetes.io/aws-load-balancer-backend-protocol": "tcp","service.beta.kubernetes.io/aws-load-balancer-ssl-cert": "'$ACM_ARN'","service.beta.kubernetes.io/aws-load-balancer-ssl-ports": "https"}}}'
    
    ```
    - Update Istio Gateway 
    ```bash
    # export NEW_CLUSTER_DOMAIN=cnvrg.new.cluster.domain.example.com
    cat <<EOF | kubectl apply -ncnvrg -f -
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: cnvrg-gateway
      namespace: cnvrg
    spec:
      selector:
        istio: ingressgateway
    spec:
      servers:
      - hosts:
        - "*.$NEW_CLUSTER_DOMAIN"
        port:
          name: http
          number: 80
          protocol: HTTP
        tls:
          httpsRedirect: true
      - hosts:
        - "*.$NEW_CLUSTER_DOMAIN"
        port:
          name: https
          number: 443
          protocol: HTTP
    EOF
    
    ```  

- Restart cnvrg webapp and sidekiq pods to apply new configuration 
    ```bash
    
    kubectl delete pods -lapp=app -o=name -ncnvrg
     
    kubectl delete pods -lapp=sidekiq -ncnvrg
    
    kubectl delete pods -lapp=searchkiq -ncnvrg
  	
    ```
  
- Use the following command for printing updated configuration
    ```bash
  	output=""
    output="${ourput}\nDEFAULT_COMPUTE_CLUSTER_DOMAIN: $(kubectl get secret env-secrets -ncnvrg -o jsonpath='{.data.DEFAULT_COMPUTE_CLUSTER_DOMAIN}' | base64 -d)"
    output="${output}\nAPP_DOMAIN: $(kubectl get secret env-secrets -ncnvrg -o jsonpath='{.data.APP_DOMAIN}' | base64 -d)"
    output="${output}\nDEFAULT_URL: $(kubectl get secret env-secrets -ncnvrg -o jsonpath='{.data.DEFAULT_URL}' | base64 -d)"
    output="${output}\nCNVRG_STORAGE_ENDPOINT: $(kubectl get secret env-secrets -ncnvrg -o jsonpath='{.data.CNVRG_STORAGE_ENDPOINT}' | base64 -d)"
    output="${output}\nDEFAULT_COMPUTE_CLUSTER_HTTPS: $(kubectl get secret env-secrets -ncnvrg -o jsonpath='{.data.DEFAULT_COMPUTE_CLUSTER_HTTPS}' | base64 -d)"
    echo -e ${output} | column -s ' ' -t
    ```