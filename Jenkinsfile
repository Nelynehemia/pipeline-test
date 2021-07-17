pipeline {
  agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 main.py'
            }
        }
        stage('test') {
            steps {
                sh 'python3 testfile.py'
            }
        }
    }
}