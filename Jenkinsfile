pipeline {
  agent { docker { image 'python:3' } }
  stages {
    stage('build') {
      steps {
        echo 'build..'
      }
    }
    stage('test') {
      steps {
        sh 'python main.py'
      }
    }
  }
}