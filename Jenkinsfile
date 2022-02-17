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
    }
}