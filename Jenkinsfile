pipeline {
    agent { label 'cpu1' }
    options { timestamps() }
    parameters{
        string defaultValue: 'master', description: 'Insert branch name', name: 'branch', trim: true
    }
    environment {
        IMAGE_NAME          = "docker.io/cnvrg/cnvrg-operator"
        IMAGE_TAG           = "${branch}-$BUILD_NUMBER"
    }
    stages {
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