<script setup>
    import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth'
</script>

<template>
    <div>
        <h1>Register</h1>
        <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" v-model="email" class="form-control" id="email" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" v-model="password" class="form-control" id="password">
        </div>
        <button type="submit" @click="register" class="btn btn-primary">Submit</button>
        <button class="btn btn-primary" @click="signInWithGoogle">Sign In With Google</button>
    </div>
</template>

<script>
    export default{
        beforeCreate() {
            const auth = getAuth()
            onAuthStateChanged(auth, user => {
                if(user){
                    this.$router.push('/')
                }
            })
        },
        data(){
            return {
                email: '',
                password: '',
            }
        },
        methods: {
            register(){
                signInWithEmailAndPassword(getAuth(), this.email, this.password)
                .then(() => {
                    this.$router.push('/')
                })
            }
        },
    }
</script>