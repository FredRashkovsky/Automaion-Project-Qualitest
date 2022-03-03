pipeline {
   agent any
    stages {
        stage('Installing packages') {
            steps {
                withPythonEnv('python') {
                    sh 'pip install pytest'
                    sh 'pytest-q'
                }
            }
        }
    }
}