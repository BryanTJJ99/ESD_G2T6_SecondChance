
<template>

    <div class="d-flex flex-column flex-shrink-0 bg-light" style="width: 4.5rem; height: 93vh; position:fixed; top: 10; left: 0; z-index:3">

        <!-- <a href="/" class="d-block p-3 link-dark text-decoration-none" title="" data-bs-toggle="tooltip" data-bs-placement="right" data-bs-original-title="Icon-only">
        <svg class="bi" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
        <span class="visually-hidden">Icon-only</span>
        </a> -->
        <ul class="nav nav-pills nav-flush flex-column mb-auto text-center">
        <li class="nav-item">
            <router-link to="/" class="nav-link py-4" >
                <i class="fas fa-home"  style="color:black"></i>
            </router-link>
        </li>
        <li>
            <router-link to="/marketplace" class="nav-link py-4" >
                <i class="fa-solid fa-store" style="color:black" ></i>
            </router-link>
        </li>
        <li>
            <router-link to="/inventory" class="nav-link py-4" >
                <i class="fa-solid fa-list" style="color:black"></i>
            </router-link>

        </li>
        <li>
            <router-link to="/chat" class="nav-link py-4" >
                <i class="fa-solid fa-message" style="color:black"></i>
            </router-link>
        </li>
        <li>
            <a href="#" class="nav-link py-4" title="" data-bs-toggle="tooltip" data-bs-placement="right" data-bs-original-title="Customers">
                <i class="fa-solid fa-gear" style="color:black"></i>
            </a>
        </li>
        </ul>
        <div class="dropdown border-top">
        <a href="#" class="d-flex align-items-center justify-content-center p-3 link-dark text-decoration-none dropdown-toggle" id="dropdownUser3" data-bs-toggle="dropdown" aria-expanded="false">
            <img src="https://github.com/mdo.png" alt="mdo" width="24" height="24" class="rounded-circle">
        </a>
        <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser3">
            <!-- <li><a class="dropdown-item" href="#">New project...</a></li>
            <li><a class="dropdown-item" href="#">Settings</a></li> -->
            <li><a class="dropdown-item" href="#">Profile</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Sign out</a></li>
        </ul>
        </div>
    </div>
</template>

<script>
  import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth'

  export default {
    data(){
      return{
            department : "Finance",
            organization : "SMU",
      }
    },
    
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