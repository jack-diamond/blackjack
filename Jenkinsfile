pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('Build') {
      steps {
        sh 'pip install --upgrade pip'
        sh 'pip install coverage'
        sh 'python -m py_compile table.py card.py blackjackplayer.py dealer.py deck.py player.py'
        sh 'python -m coverage xml -o reports/coverage.xml'
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
  post {
        always {
            junit '**/nosetests.xml'
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '**/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }
    }
}