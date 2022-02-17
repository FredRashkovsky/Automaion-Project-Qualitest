pipeline {
   agent any
    parameters{
        string(name: 'runs', defaultValue: '3' , trim: true)
    }
    stages {
        stage('build') {
            steps {
            bat "% echo ${params.runs} | test_case.py --headless"
            mail bcc: '', body: 'test was ok!', cc: '', from: '', replyTo: '', subject: 'Pipline - test', to: 'fradik890@gmail.com'
            }

        }
    }
}