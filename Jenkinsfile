pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('Build') {
      steps {
        sh 'python -m py_compile table.py card.py blackjackplayer.py dealer.py deck.py player.py'
      }
    }
    stage('Test') {
      steps {
        sh 'python test_card.py'
        sh 'python test_player.py'
        sh 'python test_blackjackplayer.py'
        sh 'python test_dealer.py'
        sh 'python test_deck.py'
        sh 'python test_integration.py'
      }  
    }
  }
}