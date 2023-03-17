<script setup>
import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth'
</script>


<template>
    <div class="container-fluid" style="background-color: #C5DAD2; height: 100vh;">
        <div class="row">
            <div class="col-7">
                <div class="container-fluid my-auto d-lg-block d-none" style="height: 100vh;">
                    <div style="position: relative; top: 20%; text-align: right;">
                        <h4>Your go to asset <br> management <br> system.</h4>
                    </div>
                    <img src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png" alt=""
                        style="width: 60%; position: absolute; left: -100px;">
                </div>

            </div>
            <div class="col-lg-5 col-12" style="background-color:white">
                <div class="row text-center mb-5">
                    <div>
                        <h1>SecondChance</h1>
                        <form class="mt-4 px-5">
                            <div class="group">
                                <input type="text" required>
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Enter Your Email:</label>
                            </div>

                            <div class="group">
                                <input type="text" required>
                                <span class="highlight"></span>
                                <span class="bar"></span>
                                <label>Enter Your Password:</label>
                            </div>
                        </form>

                    </div>
                </div>
            </div>
    </div>

</div>

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
}
</script>