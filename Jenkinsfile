// Jenkinsfile
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'dummy-devops-app'
        DOCKER_REGISTRY_CREDENTIALS_ID = 'GITHUB_CREDENTIALS'
        DOCKER_HUB_REPO = 'briandf25/dummy-devops-app'
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
