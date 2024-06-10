// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'haciendodevops/dummy-app'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }   
    }
    environment {
        DOCKER_IMAGE = "dummy-devops-app"
        DOCKER_REGISTRY_CREDENTIALS_ID = "docker-hub-token"  // ID del token configurado en Jenkins
        DOCKER_HUB_REPO = "haciendodevops/dummy-devops-app"  // Asegúrate de que este sea el nombre correcto del repositorio en Docker Hub
        GIT_CREDENTIALS_ID = "github-credentials"
        GIT_BRANCH = "features/haciendodevops"
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
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BRANCH_NAME}", ".")
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
