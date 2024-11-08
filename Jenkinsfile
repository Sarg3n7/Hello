pipeline {
    agent any

    environment {
        // Environment variables can go here
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Compile') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Post-build') {
            steps {
                junit '**/target/test-*.xml' // Assuming Maven test reports are stored here
            }
        }
    }

    post {
        success {
            echo 'Build and Tests passed!'
        }
        failure {
            echo 'Build or Tests failed.'
        }
    }
}
