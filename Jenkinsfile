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
                 steps{
              sh 'exit 0'

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