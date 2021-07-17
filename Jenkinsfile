pipeline {
  agent any
    stages {
        stage('build') {
            steps {
                sh 'sudo apt install python-pytest'
                sh 'python3 main.py'
            }
        }
    }
}