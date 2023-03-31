import { createApp } from 'vue'
// import VTooltip from 'v-tooltip'
// import 'v-tooltip/dist/v-tooltip.css'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap'
import './assets/main.css'
import "../src/assets/fontawesome-free-6.3.0-web/css/fontawesome.css"
import "../src/assets/fontawesome-free-6.3.0-web/css/brands.css"
import "../src/assets/fontawesome-free-6.3.0-web/css/solid.css"
import "./style.css"


// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import 'firebase/auth';
// import { VTooltip } from 'v-tooltip'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDBoA3VVh5IA5pOXBPx_GnJczusXK8X-IA",
  authDomain: "esdproject-d2af7.firebaseapp.com",
  projectId: "esdproject-d2af7",
  storageBucket: "esdproject-d2af7.appspot.com",
  messagingSenderId: "833898107559",
  appId: "1:833898107559:web:90b56b941bd9a335fc0182"
};

// Initialize Firebase
initializeApp(firebaseConfig);

// import { library } from "@fortawesome/fontawesome-svg-core";
// import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// import {
//     faHome,
//     faUser,
//     faUserPlus,
//     faSignInAlt,
//     faSignOutAlt,
//     faClipboard,
//     faPlus,
//     faPenToSquare,
//     faFile,
//     faUsers,
//     faBell,
//     faMagnifyingGlass,
//   } from "@fortawesome/free-solid-svg-icons";
//   library.add(faMagnifyingGlass,faHome, faUser, faUserPlus, faSignInAlt, faSignOutAlt,faClipboard, faPlus, faPenToSquare, faUsers,faBell, faFile);


const app = createApp(App)
app.use(router)
// app.use(VTooltip)

app.mount('#app')
