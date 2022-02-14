properties([parameters([string(defaultValue: '3', name: 'runs', trim: true)])])
pipeline {
   agent any
    stages {
        stage('build') {
            steps {
            bat '% echo ${params.runs} | test_case.py --headless'
            
            }

        }
    }
}