<template>
    <nav class="navbar navbar-light d-flex justify-content-between" style="background-color:#c5dad2;">
        <div class="d-flex align-items-center">
                <img class="ms-4 me-1" src="../../assets/logo.png" style="height:20px;">
                <router-link to="/home" class="nav-link text-dark m-0 p-0" >
                    <p class="logo ">SecondChance</p>
                </router-link>
        </div>
        <div>
            <button class="btn btn-none logo" @click="signOut">Sign out</button>
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