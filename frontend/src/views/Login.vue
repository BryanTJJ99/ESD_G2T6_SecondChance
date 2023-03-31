
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
                <div class="px-3" style="margin-top:30%;">
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
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.email }}</small>
                        </div>
                        <div class="group mt-5">
                            <input type="password" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Enter Your Password:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.password }}</small>
                        </div>
                    </form>
                </div>

                <div class="my-5 pb-5">

                    <button class="btn btn-dark d-block mx-auto" style="width:250px;" v-on:click="logIn()"><span>Log
                            In</span></button>

                    <div v-if="loginError" class="text-center mt-4 mx-5"><small
                            style="color:#b00b16;font-style:italic;">{{ errMsg.login }}</small>
                    </div>
                    <div v-else></div>

                    <hr style="width:250px;" class="mx-auto my-4">

                    <small class="d-block text-center" style="font-style:italic;">Don't have an account?</small>
                    <router-link to="/register">
                        <button class="btn btn-light d-block mx-auto" style="width:250px;"
                            v-on:click="register()"><span>Register
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
import { initializeApp } from "firebase/app";
import { getDatabase, ref, set } from "firebase/database";

export default {
    data() {
        return {
            email: '',
            password: '',
            companyName: '',
            companyDept: '',
            officeLocation: '',
            errMsg: { email: '', password: '', login: '' },
            loginError: false,
            deptId: ""

        }
    },
    methods: {
        logIn() {
            console.log("login")

            if (this.checkInputs()) {
                console.log("no input error")

                const auth = getAuth();
                signInWithEmailAndPassword(getAuth(), this.email, this.password)
                    .then(() => {
                        console.log("yay")

                        // get deptId of current user with email 
                        // call department MS
                        var url = ""

                        axios.get(url, {
                            email: this.email
                        })
                        .then(response => {
                            console.log("yay")

                            this.deptId = response.data

                            // set deptId in session
                            sessionStorage.setItem("deptId", this.deptId);

                        })
                        .catch(error => {
                            console.log(error.message)
                        })

                        this.$router.push('/home')
                    })
                    .catch((error) => {
                        console.log("nay")
                        const errorCode = error.code;

                        console.log(error.message)
                        let msg = error.message.slice(22, (error.message.length) - 2)

                        if (msg == 'wrong-password') {
                            this.errMsg.login = 'Password is invalid. Please try again.'
                        } else if (msg == 'user-not-found') {
                            this.errMsg.login = 'No account registered. Please register for one first.'
                            this.email = ""
                            this.password = ""
                        } else if (msg == 'invalid-email') {
                            this.errMsg.login = 'Email is invalid. Please enter a valid email address.'
                            this.email = ""
                            this.password = ""
                        } else {
                            this.errMsg.login = 'Unsuccessful login. Please try again.'
                        }
                        this.loginError = true
                    });


            } else {

                console.log("input error")
                this.loginError = true
            }

        },
        // check user inputs
        checkInputs() {
            var check = true

            if (this.email == "") {
                this.errMsg.email = "Please enter an email."
                check = false
            } else {
                this.errMsg['email'] = ""
            }
            if (this.password == "") {
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