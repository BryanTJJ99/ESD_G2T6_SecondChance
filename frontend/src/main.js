import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap'
import './assets/main.css'
import "../src/assets/fontawesome-free-6.3.0-web/css/fontawesome.css"
import "../src/assets/fontawesome-free-6.3.0-web/css/brands.css"
import "../src/assets/fontawesome-free-6.3.0-web/css/solid.css"

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

app.mount('#app')
