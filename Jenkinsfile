pipeline {
   agent any
    stages {
        stage('build') {
            withPythonEnv('python3') {
                sh 'pip install pytest'
                sh 'pytest --html=report.html --junitxml=path -q'
            }
        }
    }
    post{
        failure {  
            mail bcc: '', body: 'test Failed', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         } 
         changed {  
             mail bcc: '', body: 'test was ok!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         }
    }
}