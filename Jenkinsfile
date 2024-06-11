pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        DOCKER_IMAGE = "haciendodevops/dummy-app_features_haciendodevops"
        DOCKER_REGISTRY_CREDENTIALS_ID = "docker-hub-token"  // ID del token configurado en Jenkins
        DOCKER_HUB_REPO = "haciendodevops/dummy-app_features_haciendodevops"
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
                    def dockerTag = "${DOCKER_IMAGE}:${env.GIT_BRANCH}".replaceAll('[^a-zA-Z0-9_.-]', '_')
                    dockerImage = docker.build(dockerTag)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    def dockerTag = "${DOCKER_IMAGE}:${env.GIT_BRANCH}"
                    def registryTag = "index.docker.io/${DOCKER_HUB_REPO}:${env.GIT_BRANCH}"
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_REGISTRY_CREDENTIALS_ID}") {
                        dockerImage.push(registryTag)
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    def registryTag = "index.docker.io/${DOCKER_HUB_REPO}:${env.GIT_BRANCH}"
                    sh "docker run -d -p 5000:5000 ${registryTag}"
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