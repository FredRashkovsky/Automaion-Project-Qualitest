pipeline {
   agent any
    stages {
        stage('build') {
            steps {
                bat "pytest --html=report.html"
            }
            
        }
    }
    post{
        failure {  
            mail bcc: '', body: 'test Failed!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         } 
         changed {  
             mail bcc: '', body: 'test was ok!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'  
         }
    }
}