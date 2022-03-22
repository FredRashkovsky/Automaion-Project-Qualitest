pipeline {
   agent any
   tools {nodejs "newman", docker { image 'python:3.10.1-alpine' }}
     parameters {
         string(name: 'apikey', defaultValue: '', description: 'api-postman-key')
     }
    stages {
        stage('build') {
            steps {
                sh "python --version"
                sh "newman run https://api.getpostman.com/collections/19310415-9ceacf35-139d-4482-b6e1-b03f6fc16651?apikey=${params.apikey} --disable-unicode"
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