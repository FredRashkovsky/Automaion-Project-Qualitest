pipeline {
   agent any
    stages {
        stage('Installing packages') {
            steps {
                withPythonEnv('C:/Users/fradi/AppData/Local/Programs/Python/Python310/') {
                    sh 'pip install pytest'
                    sh 'pytest -q'
                }
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