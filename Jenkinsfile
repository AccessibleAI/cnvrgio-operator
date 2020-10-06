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
                echo "Cleaned Up Workspace For Project"
            }
        }
        stage('Code Checkout') {
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
                    echo "========================================="
                    echo "${IMAGE_NAME}:${IMAGE_TAG}"
                    echo "========================================="
                    sh "ls -all"
                    sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-build && make docker-push"
                }
            }
        }
    }
}