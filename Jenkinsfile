pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'blackjackplayer.py card.py dealer.py deck.py player.py table.py'
      }
    }
    stage('test') {
      steps {
        sh 'python test_table.py'
      }  
    }
  }
}