pipeline {
   agent any
     parameters {
         string(name: 'apikey', defaultValue: '', description: 'api-postman-key')
     }
    stages {
        stage('build') {
            steps {
                bat "pytest --html=report.html"
                bat "export PATH=/sbin:/usr/sbin:/usr/bin:/usr/local/bin"
                bat "newman run https://api.getpostman.com/collections/19310415-9ceacf35-139d-4482-b6e1-b03f6fc16651?apikey=${params.apikey}"
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