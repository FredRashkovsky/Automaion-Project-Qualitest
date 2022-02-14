pipeline {
    agent 'node:16.13.1-alpine'
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh '% echo 3 | test_case.py --headless'
            }
        }
    }
}