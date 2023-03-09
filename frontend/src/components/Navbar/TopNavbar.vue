<template>
    <nav class="navbar navbar-light bg-light d-flex justify-content-between">
        <div class="d-flex justify-content-start">
            <img src="../../assets/logo.png" style="height:20px;opacity:70%">
            <div>
                <router-link to="/home" class="nav-link text-dark p-2 mx-3" >
                    <p class="logo">SecondChance</p>
                </router-link>
            </div>
        </div>
        <div>
            <button class="btn btn-none" @click="signOut">Sign out</button>
        </div>
        
    </nav>
</template>

<script>
  import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'
  export default {
    methods: {
      signOut(){
        const auth = getAuth()
        signOut(auth).then(() => {
          console.log('Sign out complete')
        })
      }
    }
  }
</script>