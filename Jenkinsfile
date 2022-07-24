pipeline {
    agent any
    environment {
        PROJECT_ID = 'mlops-353417'
        CLUSTER_NAME = 'training-cluster'
        LOCATION = 'us-central1-a'
        CREDENTIALS_ID = 'AutomaticTrainingCICD'
    }
    stages {
        stage('Cloning our Git') {
            steps {
                git url: 'https://github.com/sam2881/deployment.git', branch: 'master'
            }
        }
        stage('Building and deploying image') {
            steps {
                script {
                    docker.withRegistry('https://gcr.io', 'gcr:AutomaticTrainingCICD') {
                        app = docker.build('automatictrainingcicd/prediction-api')
                        app.push("latest")
                    }
                }
            }
        }
        stage('Deploying to GKE') {
            steps{
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'pod.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
            }
        }
    }