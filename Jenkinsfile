pipeline {
   agent any
    stages {
        stage('build') {
            steps {
                bat '\'% echo $runs | test_case.py --headless\''
            }
        }
    }
}