<script setup>
import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth'
</script>


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
                <div class="text-center px-3" style="margin-top:25%;">
                    <img src="../assets/logo.png" style="height:50px;opacity:50%;">
                    <h3 class="mt-1">SecondChance</h3>
                    <form class="mt-5 px-5">
                        <div class="group">
                            <input type="text" v-model="email" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Enter Your Email:</label>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Enter Your Password:</label>
                        </div>
                    </form>
                </div>

                <div class="mb-5 pb-5">
                    <button class="btn btn-none d-block mx-auto mt-5" style="width:250px;"
                        @click="signInWithGoogle"><span>Sign In With Google</span></button>
                    <button class="btn btn-dark d-block mx-auto mb-5" style="width:250px;"><span>Log In</span></button>

                    <hr style="width:250px;" class="mx-auto my-0">

                    <small class="d-block text-center mt-4" style="font-style:italic;">Don't have an account?</small>
                    <router-link to="/register">
                        <button class="btn btn-light d-block mx-auto" style="width:250px;"><span>Register
                                Here</span></button></router-link>
                </div>
            </div>
        </div>
    </div>
    <Footer></Footer>


<!-- <h1>Register</h1>
        <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" v-model="email" class="form-control" id="email" aria-describedby="emailHelp">
                        </div>
        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" v-model="password" class="form-control" id="password">
                        </div> -->
    <!-- <button type="submit" @click="register" class="btn btn-primary">Submit</button>
                        <button class="btn btn-primary" @click="signInWithGoogle">Sign In With Google</button> -->
</template>

<script>
import Footer from "@/components/Footer.vue";

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
        }
    },
    methods: {
        register() {
            signInWithEmailAndPassword(getAuth(), this.email, this.password)
                .then(() => {
                    this.$router.push('/')
                })
        }
    },
    components: {
        Footer
    }
}
</script>