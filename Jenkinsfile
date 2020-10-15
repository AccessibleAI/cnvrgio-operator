def CURRENT_VERSION
def NEXT_VERSION
def TESTS_PASSED = "true"
pipeline {
    agent { label 'cpu1' }
    options { timestamps() }
    environment {
        IMAGE_NAME = "docker.io/cnvrg/cnvrg-operator"
        CLUSTER_LOCATION = "northeurope"
        CLUSTER_NAME = "${env.BRANCH_NAME}.replaceAll("_", "-")-$BUILD_NUMBER"
        NODE_COUNT = 2
        NODE_VM_SIZE = "Standard_D8s_v3"
    }
    stages {
        stage('cleanup workspace') {
            steps {
                cleanWs()
            }
        }
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('set globals') {
            steps {
                script {
                    if (env.BRANCH_NAME == "master" || env.BRANCH_NAME == "develop") {
                        CURRENT_VERSION = sh(script: 'git fetch && git tag -l --sort -version:refname | head -n 1', returnStdout: true).trim()
                        def nextVersion = sh(script: "scripts/semver.sh bump minor ${CURRENT_VERSION}", returnStdout: true).trim()
                        if (env.BRANCH_NAME == "master") {
                            NEXT_VERSION = "${nextVersion}"
                        }
                        if (env.BRANCH_NAME == "develop") {
                            NEXT_VERSION = "${nextVersion}-rc1"
                        }
                    } else {
                        CURRENT_VERSION = sh(script: 'git fetch && git tag -l --sort -version:refname | grep -v rc | head -n 1', returnStdout: true).trim()
                        NEXT_VERSION = "${CURRENT_VERSION}-${env.BRANCH_NAME}-$BUILD_NUMBER"
                    }
                    echo "NEXT VERSION: ${NEXT_VERSION}"
                }
            }
        }
        stage('build image') {
            steps {
                script {
                    sh "ls -all"
                    sh "TAG=${NEXT_VERSION} make docker-build"
                }
            }
        }
        stage('push image') {
            steps {
                script {
                    sh "TAG=${NEXT_VERSION} make docker-push"
                }
            }
        }
        stage('setup test cluster') {
            steps {
                script {
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
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        TESTS_PASSED = "false"
                        def testDiscoveryPattern = "test_*"
                        if (env.BRANCH_NAME != "develop" && env.BRANCH_NAME != "master" && !env.BRANCH_NAME.startsWith("PR-")) {
                            testDiscoveryPattern = env.BRANCH_NAME
                            testDiscoveryPattern = "*${testDiscoveryPattern}*".replaceAll("-", "_").toLowerCase()
                        }
                        sh """
                        docker pull cnvrg/cnvrg-operator-test-runtime:latest
                        docker run \
                        -eTAG=${NEXT_VERSION} \
                        -v ${workspace}:/root \
                        -v ${workspace}/kubeconfig:/root/.kube/config \
                        cnvrg/cnvrg-operator-test-runtime:latest \
                        python tests/run_tests.py --test-discovery-pattern ${testDiscoveryPattern}
                        """
                        TESTS_PASSED = "true"
                    }
                }
            }
        }
        stage('store tests report ') {
            steps {
                script {
                    withCredentials([string(credentialsId: '85318dfa-3ae8-4384-b7b8-0fcc8fab0b3a', variable: 'ACCOUNT_KEY')]) {
                        sh """
                        az storage blob upload \
                         --account-name operatortestreports \
                         --container-name reports \
                         --name ${NEXT_VERSION}.html \
                         --file "tests/reports/\$(ls tests/reports)" \
                         --account-key ${ACCOUNT_KEY}
                        """
                        echo "https://operatortestreports.blob.core.windows.net/reports/${NEXT_VERSION}.html"
                    }
                }
            }
        }
        stage('generate helm chart') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'charts-cnvrg-io', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh """
                        helm repo add cnvrg https://charts.cnvrg.io
                        helm repo update
                        VERSION=${NEXT_VERSION} envsubst < chart/Chart.yaml | tee tmp-file && mv tmp-file chart/Chart.yaml
                        helm push chart cnvrg -u=${USERNAME} -p=${PASSWORD} --force
                        helm repo update
                        helm search repo cnvrg -l --devel
                        """
                    }
                }
            }
        }
        stage('bump version') {
            when {
                expression { return ((env.BRANCH_NAME == "develop" || env.BRANCH_NAME == "master") && TESTS_PASSED.equals("true")) }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '9e673d23-974c-460c-ba67-1188333cf4b4', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        def url = sh(returnStdout: true, script: 'git config remote.origin.url').trim().replaceAll("https://", "")
                        sh """
                        git tag -a ${NEXT_VERSION} -m "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
                        git push https://${USERNAME}:${PASSWORD}@${url} --tags
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