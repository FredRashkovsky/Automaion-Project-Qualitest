pipeline {
   agent any
    stages{
        stage('build') {
            steps {
                sh 'python -m pytest -q'      
            }
        }
    }
}