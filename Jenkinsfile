pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DOCKER_IMAGE = "dummy-app"
        DOCKER_REGISTRY_CREDENTIALS_ID = "docker-hub-token"  // ID del token configurado en Jenkins
        DOCKER_HUB_REPO = "haciendodevops/dummy-app"
        GIT_CREDENTIALS_ID = "github-credentials"
        GIT_BRANCH = "features/haciendodevops"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${env.GIT_BRANCH}", url: 'https://github.com/haciendodevops/02-JenkinsPipeline.git', credentialsId: "${GIT_CREDENTIALS_ID}"
            }
        }
        stage('Print User') {
            steps {
                script {
                    sh 'whoami'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_REGISTRY_CREDENTIALS_ID}") {
                        dockerImage.push("${env.GIT_BRANCH}")
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}:latest"
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
