pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                gv = load "main.py"
                gv.print_hi(name)
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