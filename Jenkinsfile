// Jenkinsfile
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "${env.DOCKER_IMAGE}"
        DOCKER_REGISTRY_CREDENTIALS_ID = "${env.DOCKER_REGISTRY_CREDENTIALS_ID}"
        DOCKER_HUB_REPO = "${env.DOCKER_HUB_REPO}"
    }


    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${env.GIT_BRANCH}", url: 'https://github.com/haciendodevops/02-JenkinsPipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BRANCH_NAME}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_REGISTRY_CREDENTIALS_ID) {
                        dockerImage.push("${env.BRANCH_NAME}")
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${DOCKER_HUB_REPO}:${env.BRANCH_NAME}"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
