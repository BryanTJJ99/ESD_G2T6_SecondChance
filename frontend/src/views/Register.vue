<script setup>
import { getAuth, createUserWithEmailAndPassword, updateProfile } from 'firebase/auth'
</script>

<template>
    <header style="background-color:#6e9190;" class="text-center">
        <small style="color:white;">Join SecondChance today and manage your company's assets.</small>
    </header>
    <div class="container-fluid" style="background-color: #C5DAD2; height: 120vh;">
        <div class="row">
            <div class="col-7">
                <div class="container-fluid my-auto d-lg-block d-none" style="height: 100vh;">
                    <div style="position: relative; top: 15%; text-align: right;" class="pe-5">
                        <h4>Track your carbon emissions.</h4>
                        <h4>Give unwanted items <br> a second chance.</h4>
                    </div>
                    <img src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png" alt=""
                        style="width: 60%; position: absolute; left: -100px;">
                </div>

            </div>
            <div class="col-lg-5 col-12" style="background-color:white;border-radius: 0px 0px 0px 15px;">
                <div class="text-center px-3" style="margin-top:15%;">
                    <img src="../assets/logo.png" style="height:50px;opacity:50%;">
                    <h3 class="mt-1">SecondChance</h3>
                    <form class="mt-5 px-5">
                        <div class="group">
                            <input type="text" v-model="email" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Email:</label>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Password:</label>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Company Name:</label>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Company Department:</label>
                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Office Location:</label>
                        </div>
                    </form>
                </div>

                <div class="my-5 pt-2">
                    <button class="btn btn-dark d-block mx-auto" style="width:250px;"><span>Register Now</span></button>
                </div>
            </div>
        </div>

    </div>
    <Footer></Footer>

<!-- <div>
        <h1>Register</h1>
        <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" v-model="email" class="form-control" id="email" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" v-model="password" class="form-control" id="password">
        </div>
            <p v-if="errMsg">{{ errMsg }}</p>
            <button type="submit" @click="register" class="btn btn-primary">Submit</button>
            <button class="btn btn-primary" @click="signInWithGoogle">Sign In With Google</button>
        </div> -->
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
    data() {
        return {
            email: '',
            password: '',
            errMsg: ''
        }
    },
    methods: {
        register() {
            createUserWithEmailAndPassword(getAuth(), this.email, this.password)
                .then(() => {
                    this.$router.push('/')
                })
                .catch((err) => {
                    switch (err.code) {
                        case "auth/email-already-in-use":
                            this.errMsg = 'Email is already in use'
                            break
                    }
                })
        }
    },
    components: {
        Footer
    }
}
</script>