pipeline {
   agent any
    stages {
        stage('build') {
            steps {
            properties([parameters([string(defaultValue: '3', name: 'runs', trim: true)])])
            bat '% echo ${runs} | test_case.py --headless'            
            
            }

        }
    }
}