pipeline {
    agent {'python:3.10.0-alpine'}
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh '% echo 3 | test_case.py --headless'
            }
        }
    }
}