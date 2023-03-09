<script setup>
    import { getAuth, signInWithEmailAndPassword, updateProfile, onAuthStateChanged } from 'firebase/auth'
</script>


<template>
    <div class="container-fluid" style="background-color: #C5DAD2; height: 100vh;">
       <div class="row">
        <div class="col-7">
            <div class="container-fluid my-auto d-lg-block d-none" style="height: 100vh;">
                <div style="position: relative; right:200px; inherit; top: 200px; text-align: right;"> 
                    <p>Your go to asset <br> management <br> system.</p>
                 </div>
                <img src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png" alt="" style="width: 60%; position: absolute; left: -100px; top:-50px;">
            </div>
            
        </div>
        <div class="col-lg-5 col-12 p-0 d-flex align-items-center" >
            <div class="p-3" style="width: 100%;">
                <div class="text-center mb-5"> <h1>SecondChance</h1></div>
                <div class="mb-3 ">
                    <small class="m-1">Email</small>
                    <div class="input-group">
                        <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">
                    </div>
                </div>
                <div class="mb-3 ">
                    <small class="m-1">Password</small>
                    <div class="input-group">
                        <input type="password" class="form-control" id="basic-url" aria-describedby="basic-addon3">
                    </div>
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