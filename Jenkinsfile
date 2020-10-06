pipeline {
    agent { label 'cpu1' }
    options { timestamps() }
    environment {
        IMAGE_NAME          = "docker.io/cnvrg/cnvrg-operator"
        IMAGE_TAG           = "${env.BRANCH_NA}-$BUILD_NUMBER"
    }
    stages {
        stage('Cleanup Workspace') {
            steps {
                cleanWs()
                sh "echo 'Cleaned Up Workspace For Project'"
                sh "echo 'Cleaned Up Workspace For Project'"
                sh "echo 'Cleaned Up Workspace For Project'"
                sh "echo 'Cleaned Up Workspace For Project'"
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
                    sh "ls -all"
                    sh "IMG=${IMAGE_NAME}:${IMAGE_TAG} make docker-build && make docker-push"
                }
            }
        }
    }
}