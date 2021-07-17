pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Nelynehemia/pipeline-test.git']]])
            }
        }
        stage('Build') {
            steps {
                git 'https://github.com/Nelynehemia/pipeline-test.git'
                sh 'python main.py'
            }
        }
        stage('Test'){
            steps {
                echo 'the job hes been tested '
            }
        }

    }
}
