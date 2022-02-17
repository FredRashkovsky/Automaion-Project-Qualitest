pipeline {
   agent { docker { image 'python:3.10.1-alpine' } }
    parameters{
        string(name: 'runs', defaultValue: '3' , trim: true)
    }
    stages {
        stage('build') {
            steps {
            bat "% echo ${params.runs} | test_case.py --headless"
            
            }

        }
    }
}