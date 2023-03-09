<template>
    <nav class="navbar navbar-light bg-light d-flex justify-content-between" style="position: sticky; top: 0;">
        <div class="d-flex align-items-center">
                <img class="ms-4 me-1" src="../../assets/logo.png" style="height:20px;">
                <router-link to="/" class="nav-link text-dark m-0 p-0" >
                    <p class="logo ">SecondChance</p>
                </router-link>
        </div>
        <div>
          <small>{{ organization }}  |  {{ department }}</small>
            <button class="btn btn-none logo" @click="signOut">Sign out</button>
        </div>
        
    </nav>
</template>

<script>
  import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'
  export default {
    data(){

    },
    methods: {
      signOut(){
        const auth = getAuth()
        signOut(auth).then(() => {
          console.log('Sign out complete')
        })
      }
    },
    props:['organization', 'department']
  }
</script>