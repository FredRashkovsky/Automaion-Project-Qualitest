pipeline {
   agent any
    stages {
        stage('build') {
            steps {
                bat "pytest --html=report.html"
                bat 'newman run https://api.getpostman.com/collections/19310415-9ceacf35-139d-4482-b6e1-b03f6fc16651?apikey=PMAK-6231d0b277fb913ff4f5503f-c3af470ee838ca87e0a54f22e039938567'
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