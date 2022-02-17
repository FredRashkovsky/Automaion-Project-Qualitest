pipeline {
   agent any
    parameters{
        string(name: 'runs', defaultValue: '3' , trim: true)
    }
    stages {
        stage('build') {
            steps {
            bat "% echo ${params.runs} | test_case.py --headless"
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