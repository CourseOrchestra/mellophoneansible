node {
   stage ("Get Latest Code") {
      checkout scm
   }
   
   try {
     stage ("Molecule test") {
        /* Jenkins checks out the role into 
        a folder with arbitrary name, so we need to
        let Ansible know where to find 'mellophoneansible' role*/
        sh 'mkdir -p molecule/default/roles'
        sh 'ln -sf `pwd` molecule/default/roles/mellophoneansible'
        sh 'molecule test'
     }
   } catch(all) {
      currentBuild.result = "FAILURE"
      throw err
   }
}