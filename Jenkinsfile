pipeline {
    agent { label 'cpu1' }
    options { timestamps() }
    environment {
        IMAGE_NAME          = "docker.io/cnvrg/cnvrg-operator"
        IMAGE_TAG           = "${env.BRANCH_NAME}-$BUILD_NUMBER"
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
//         stage('build image') {
//             steps {
//                 script {
//                     sh "ls -all"
//                     sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-build"
//                 }
//             }
//         }
//         stage('push image') {
//             steps {
//                 script {
//                     sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-push"
//                 }
//             }
//         }
        stage('Build AKS CLUSTER') {
            steps {
//                 script{
                    withCredentials([azureServicePrincipal('jenkins-cicd-azure-new')]) {
                        echo "${$AZURE_CLIENT_ID} ${AZURE_CLIENT_SECRET} ${AZURE_TENANT_ID}"
                        sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID'
    //                     sh 'az account set -s $AZURE_SUBSCRIPTION_ID'
    //                     sh "az group create --location ${globalvars["aks"].LOCATION} --name ${CLUSTER_NAME}"
    //                     sh "az aks create --resource-group  ${CLUSTER_NAME} --name ${CLUSTER_NAME} --location ${globalvars["aks"].LOCATION} --node-count ${NODE_COUNT} --node-vm-size ${globalvars["aks"].NODE_VM_SIZE} --service-principal ${AZURE_CLIENT_ID} --client-secret ${AZURE_CLIENT_SECRET}"
    //                     sh "az aks get-credentials --resource-group ${CLUSTER_NAME} --name ${CLUSTER_NAME} --file ${globalvars["global"].kubeconfig} --subscription $AZURE_SUBSCRIPTION_ID"
                    }
//                 }
            }
        }
//         stage('setup test cluster') {
//             steps {
//                 script {
//                     sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-push"
//                 }
//             }
//         }
    }
}