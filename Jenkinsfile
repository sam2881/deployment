pipeline {
    agent any
    environment {
        PROJECT_ID = 'mlops-353417'
        CLUSTER_NAME = 'training-cluster'
        LOCATION = 'us-west1'
        CREDENTIALS_ID = 'AutomaticTrainingCICD'
    }
    stages {
        stage('Cloning our Git') {
            steps {
                git url: 'https://github.com/sam2881/deployment.git', branch: 'master'
            }
        }
        stage('Building and Pushing to Registry') {
            steps {
                script {
                    docker.withRegistry('https://gcr.io', 'gcr:AutomaticTrainingCICD') {
                        app = docker.build('mlops-353417/prediction-api')
                        app.push("latest")
                        echo "Complete"
                    }
                }
            }
        }
     stage('Deploy to staging area') {
            steps{
              sh 'exit 0'

                }
            }

             stage('Load Test') {
            steps{
              sh 'exit 0'

                }
            }
    }

    }