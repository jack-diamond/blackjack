pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'python -m py_compile table.py'
      }
    }
    stage('test') {
      steps {
        sh 'python test_card.py test_player.py'
      }  
    }
  }
}