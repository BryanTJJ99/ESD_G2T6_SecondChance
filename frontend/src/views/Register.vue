<script setup>
    import { getAuth, createUserWithEmailAndPassword, updateProfile } from 'firebase/auth'
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
        <p v-if="errMsg">{{ errMsg }}</p>
        <button type="submit" @click="register" class="btn btn-primary">Submit</button>
        <button class="btn btn-primary" @click="signInWithGoogle">Sign In With Google</button>
    </div>
</template>

<script>
    export default{
        data(){
            return {
                email: '',
                password: '',
                errMsg: ''
            }
        },
        methods: {
            register(){
                createUserWithEmailAndPassword(getAuth(), this.email, this.password)
                .then(() => {
                    this.$router.push('/')
                })
                .catch((err) => {
                    switch(err.code){
                        case "auth/email-already-in-use":
                            this.errMsg = 'Email is already in use'
                            break
                    }
                })
            }
        },
    }
</script>