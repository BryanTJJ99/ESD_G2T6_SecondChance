<script setup>
    import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth'
</script>


<template>
    <div class="container-fluid p-0 m-0" style="background-color: #C5DAD2; height: 100vh;">
       <div class="row">
        <div class="col-8">
            <div class="container-fluid my-auto d-md-inline d-none" style="height: 100vh;">
                <div style="position: relative; right:200px; inherit; top: 200px; text-align: right;"> 
                    <p>Your go to asset <br> management <br> system.</p>
                 </div>
                <img src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png" alt="" style="width: 60%; position: absolute; left: -100px;">
            </div>
            
        </div>
        <div class="col-md-4 col-12" >
            <div>
                HI
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