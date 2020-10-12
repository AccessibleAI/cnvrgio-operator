pipeline {
    agent { label 'cpu1' }
    options { timestamps() }
    environment {
        IMAGE_NAME          = "docker.io/cnvrg/cnvrg-operator"
        IMAGE_TAG           = "${env.BRANCH_NAME}-$BUILD_NUMBER"
        CLUSTER_LOCATION    = "northeurope"
        CLUSTER_NAME        = "${env.BRANCH_NAME}-$BUILD_NUMBER"
        NODE_COUNT          = 2
        NODE_VM_SIZE        = "Standard_D8s_v3"
    }
    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                echo "Cleaned up workspace for project"
            }
        }
        stage('checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: scm.branches,
                    userRemoteConfigs: [[url: 'https://github.com/AccessibleAI/cnvrgio-operator.git']]
                ])
            }
        }
        stage('build image') {
            steps {
                script {
                    sh "ls -all"
                    sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-build"
                }
            }
        }
        stage('push image') {
            steps {
                script {
                    sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-push"
                }
            }
        }
        stage('setup test cluster') {
            when {
                not {
                    changelog '.*skip tests.*'
                }
            }
            steps {
                script{
                    withCredentials([azureServicePrincipal('jenkins-cicd-azure-new')]) {
                        sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
                        sh 'az account set -s $AZURE_SUBSCRIPTION_ID'
                        sh "az group create --location ${CLUSTER_LOCATION} --name ${CLUSTER_NAME}"
                        sh "az aks create --resource-group  ${CLUSTER_NAME} --name ${CLUSTER_NAME} --location ${CLUSTER_LOCATION} --node-count ${NODE_COUNT} --node-vm-size ${NODE_VM_SIZE} --service-principal ${AZURE_CLIENT_ID} --client-secret ${AZURE_CLIENT_SECRET}"
                        sh "az aks get-credentials --resource-group ${CLUSTER_NAME} --name ${CLUSTER_NAME} --file kubeconfig --subscription $AZURE_SUBSCRIPTION_ID"
                    }
                }
            }
        }
        stage('run tests') {
            when {
                not {
                    changelog '.*skip tests.*'
                }
            }
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        def testDiscoveryPattern = "test_*"
                        if (env.BRANCH_NAME != "develop" && env.BRANCH_NAME != "master"){
                            testDiscoveryPattern = env.BRANCH_NAME
                            testDiscoveryPattern = "*${testDiscoveryPattern}*".replaceAll("-","_").toLowerCase()
                        }
                        sh """
                        docker run \
                        -eTAG=${IMAGE_TAG} \
                        -v ${workspace}:/root \
                        -v ${workspace}/kubeconfig:/root/.kube/config \
                        cnvrg/cnvrg-operator-test-runtime:latest \
                        python tests/run_tests.py --test-discovery-pattern ${testDiscoveryPattern}
                        """
                    }
                }
            }
        }
        stage('store tests report ') {
            when {
                not {
                    changelog '.*skip tests.*'
                }
            }
            steps {
                script {
                    withCredentials([string(credentialsId:'85318dfa-3ae8-4384-b7b8-0fcc8fab0b3a', variable: 'ACCOUNT_KEY')]) {
                        sh """
                        az storage blob upload \
                         --account-name operatortestreports \
                         --container-name reports \
                         --name ${IMAGE_TAG}.html \
                         --file "tests/reports/\$(ls tests/reports)" \
                         --account-key ${ACCOUNT_KEY}
                        """
                        echo "https://operatortestreports.blob.core.windows.net/reports/${IMAGE_TAG}.html"
                    }
                }
            }
        }
        stage('generate helm chart') {
            steps {
                script {
                    def version = "${IMAGE_TAG}"
                    withCredentials([usernamePassword(credentialsId: 'charts-cnvrg-io', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh """
                            helm repo add cnvrg https://charts.cnvrg.io
                            helm repo update
                            VERSION=${version} envsubst  < chart/Chart.yaml  | tee  chart/Chart.yaml
                            VERSION=${version} envsubst  < chart/values.yaml | tee  chart/values.yaml
                            helm push chart cnvrg -u=${USERNANE} -p=${PASSWORD}
                        """

                    }
                }
            }
        }
    }
    post {
        success {
            script {
                echo "Success!"
            }
        }
        failure {
            script {
                echo 'Failed!'
            }
        }
        always {
            script {
                withCredentials([azureServicePrincipal('jenkins-cicd-azure-new')]) {
                    sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
                    sh 'az account set -s $AZURE_SUBSCRIPTION_ID'
                    sh """
                    if [ \$(az group list -o table  | grep ^${CLUSTER_NAME} | wc -l)  -gt 0 ]
                    then
                        echo "deleting aks cluster..."
                        az group delete --name ${CLUSTER_NAME} --no-wait -y
                    else
                        echo "cluster not found, skipping cluster delete"
                    fi
                    """
                }
            }
        }
    }
}