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
        stage('artifact to s3') {
            steps{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'nelys3', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh 'aws s3 ls'
                    //sh 'aws s3 mb s3://nely-bucket'
                    //sh 'aws s3 cp pipeline-test/main.py s3://nely-bucket'
                }
            }
        }
    }
}