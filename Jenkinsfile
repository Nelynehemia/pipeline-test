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
            try{
                withCredentials([aws(accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: 'nelys3', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh "aws s3 ls"
                    sh "aws s3 mb s3://cloudyeti-bucken-for-aws"
                    //sh "aws s3 cp"
                }
            } catch(err){
                sh "echo error in sending artifact to s3"
            }
        }
    }
}