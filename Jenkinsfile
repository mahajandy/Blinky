    
pipeline {
    agent { docker { image  'shurikg/python-pyodbc' } }
  environment {HOME = '/tmp'} 
  stages {
    // First stage , get files from your GitHub repository.
    stage('Git'){
        steps{
            checkout scm
        }
    }
    stage('build') {
        steps {
        sh 'pip install --user --no-cache-dir -r requirements.txt'
      }
    }
    stage('test') {
        steps {
            sh 'python UnitTest.py'
        
      }
    }
/*
    stage('Commits') {
        steps {
        dir("Hackaton_2019") {
            sh 'python Commits.py'
        }
        
      }
    }
 
    stage('transperent') {
        steps {
            dir("Hackaton_2019") {
                 sh 'python transperent.py'
            }
        
      }
    }
    stage('Benchmark') {
        steps {
        dir("Hackaton_2019") {
            sh 'python Benchmark.py'
        }
        
      }
    }
    stage('Evaluation') {
        steps {
        dir("Hackaton_2019") {
            sh 'python Evaluation.py'
        }
        
      }
    }
      */
  }
}
