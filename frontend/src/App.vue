<script setup>
</script>

<template>
  <div>
    <header>
      <!-- <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>
              <router-link to="/chat" class="nav-link">Chat</router-link>
            </div>
          </div>
        </div>
      </nav> -->
    </header>
    <div class="container-fluid">
      <button class="btn btn-primary" @click="signOut">Sign out</button>
      <RouterView />
    </div>
  </div>
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

<style scoped>

</style>
