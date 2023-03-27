
<template>
    <header style="background-color:#6e9190;" class="text-center">
        <small style="color:white;">Track your carbon emissions. Give unwanted items a second chance.</small>
    </header>
    <div class="container-fluid" style="background-color: #C5DAD2;height: 120vh;">
        <div class="row">
            <div class="col-7">
                <div class="container-fluid my-auto d-lg-block d-none" style="height: 100vh;">
                    <div style="position: relative; top: 15%; text-align: right;" class="pe-5">
                        <h4>Your go to asset <br> management <br> system.</h4>
                    </div>
                    <img src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png" alt=""
                        style="width: 60%; position: absolute; left: -100px;">
                </div>

            </div>
            <div class="col-lg-5 col-12" style="background-color:white;border-radius: 0px 0px 0px 15px;">
                <div class="px-3" style="margin-top:25%;">
                    <div class="text-center">
                        <img src="../assets/logo.png" style="height:50px;opacity:50%;">
                        <h3 class="mt-1 text-center">SecondChance</h3>

                    </div>
                    <form class="mt-5 px-5">
                        <div class="group">
                            <input type="text" v-model="email" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Enter Your Email:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{errMsg.email}}</small>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Enter Your Password:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{errMsg.password}}</small>
                        </div>
                    </form>
                </div>

                <div class="mb-5 pb-5">
                    <button class="btn btn-none d-block mx-auto mt-5" style="width:250px;"
                        @click="signInWithGoogle"><span>Sign In With Google</span></button>
                    <button class="btn btn-dark d-block mx-auto mb-5" style="width:250px;" v-on:click="logIn()"><span>Log In</span></button>

                    <hr style="width:250px;" class="mx-auto my-0">

                    <small class="d-block text-center mt-4" style="font-style:italic;">Don't have an account?</small>
                    <router-link to="/register">
                        <button class="btn btn-light d-block mx-auto" style="width:250px;" v-on:click="register()"><span>Register
                                Here</span></button></router-link>
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>

</template>

<script>
import Footer from "@/components/Footer.vue";
import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth';


export default {
    beforeCreate() {
        const auth = getAuth()
        onAuthStateChanged(auth, user => {
            if (user) {
                this.$router.push('/')
            }
        })
    },
    data() {
        return {
            email: '',
            password: '',
            companyName: '',
            companyDept: '',
            officeLocation: '',
            errMsg: {email:'', password:''},
            
        }
    },
    methods: {
        logIn(){
            console.log("login")

            if (this.checkInputs()){
                console.log("no input error")
            } else {
                console.log("input error")
            }

        },
        signInWithGoogle(){
            console.log("sign in with google")

            signInWithEmailAndPassword(getAuth(), this.email, this.password)
            .then(() => {
                this.$router.push('/')
            })
        },
        // check user inputs
        checkInputs(){
            var check = true

            if (this.email == ""){
                this.errMsg.email = "Please enter an email."
                check = false
            } else {
                this.errMsg['email'] = ""
            }
            if (this.password == ""){
                this.errMsg['password'] = "Please enter a password."
                check = false
            } else {
                this.errMsg['password'] = ""
            }

            return check
        }
    },
    components: {
        Footer
    }
}
</script>