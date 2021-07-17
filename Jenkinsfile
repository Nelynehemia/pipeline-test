pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        echo 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python main.py'
      }
    }
  }
}