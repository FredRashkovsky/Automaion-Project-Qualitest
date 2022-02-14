pipeline {
    agent any { image 'python:3.10.1-alpine' }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh '% echo 3 | test_case.py --headless'
            }
        }
    }
}