pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                print_hi(name)
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}