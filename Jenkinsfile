pipeline {
   agent any
    stages {
        stage('build') {
            steps {
                bat '% echo 3 | test_case.py --headless'
            }
        }
    }
}