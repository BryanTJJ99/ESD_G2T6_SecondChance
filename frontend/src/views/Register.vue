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
                <div class="px-3" style="margin-top:15%;">
                    <div class="text-center">
                        <img src="../assets/logo.png" style="height:50px;opacity:50%;">
                        <h3 class="mt-1 text-center">SecondChance</h3>

                    </div>
                    <form class="my-5 px-5">
                        <div class="group">
                            <input type="text" v-model="email" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Email:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.email }}</small>
                        </div>
                        <div class="group mt-5">
                            <input type="password" v-model="password" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Password:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.password }}</small>

                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="companyName" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Company Name:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.companyName
                            }}</small>

                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="companyDept" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Company Department:</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.companyDept
                            }}</small>

                        </div>
                        <div class="group mt-5">
                            <input type="text" v-model="officeLocation" required>
                            <span class="highlight"></span>
                            <span class="bar"></span>
                            <label>Your Office Location (Postal Code):</label>
                            <small class="text-start" style="color:#b00b16;font-style:italic;">{{ errMsg.officeLocation
                            }}</small>
                        </div>
                    </form>
                </div>

                <div class="pb-5">
                    <div class="pt-2">
                        <button class="btn btn-dark d-block mx-auto" style="width:250px;"
                            v-on:click="registerMe()"><span>Register Now</span></button>
                    </div>

                    <div v-if="valid"></div>
                    <div v-else class="text-center pt-2 mx-5"><small style="color:#b00b16;font-style:italic;">{{
                        errMsg.valid }}</small>
                    </div>

                </div>

            </div>
        </div>

    </div>
    <Footer></Footer>
</template>

<script>
import Footer from "@/components/Footer.vue";
import { getAuth, createUserWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
import registerService from "../../services/register/registerService";

export default {
    data() {
        return {
            errMsg: { email: '', password: '', companyName: '', companyDept: '', officeLocation: '', valid: '' },
            email: '',
            password: '',
            companyName: '',
            companyDept: '',
            officeLocation: '',
            valid: true,
            deptId: '',

            companyDetails: undefined,
            departmentDetails: undefined,
            updateCompany: undefined,
            updateDepartment: undefined,
            checkCompany: undefined
        }
    },
    methods: {
        registerMe() {

            var check = this.checkInputs()

            if (check) {
                console.log("no input error")

                this.add()

                // const auth = getAuth();
                // createUserWithEmailAndPassword(getAuth(), this.email, this.password)
                //     .then(() => {
                        
                //         console.log("yay")

                //         // this.add()

                //     })
                //     .catch((err) => {
                //         console.log("nay")
                //         console.log(err)

                //         const errorCode = err.code;
                //         console.log(errorCode)

                //         if (errorCode == "auth/email-already-in-use") {
                //             this.errMsg['valid'] = "Registration failed. Email entered is already in use."

                //             this.valid = false

                //         } else if (errorCode == "auth/invalid-email") {
                //             this.errMsg['valid'] = "Registration failed. You have entered an invalid email address."

                //             this.valid = false
                //         }

                //     })

            } else {
                console.log("input error")

            }
        },
        add: async function () {

            console.log("-------------------------------")

            var data1 = {
                companyName: this.companyName,
                departments: []
            }

            var data2 = {
                departmentName: this.companyDept,
                postalCode: this.officeLocation,
                email: this.email,
                companyId: companyId,
                itemIdArrayList: [],
                totalCarbon: 0,
            }

            var checkResponse = await registerService.checkCompany(this.companyName)
            var checkCompany = checkResponse
            console.log(checkCompany)
            var companyId = ""

            // Company registered yet
            if (checkCompany){

                console.log("Company already registered")
                // console.log(checkCompany.data.departments)
                // data1["departments"] = checkCompany.data.departments
                // companyId = checkCompany.data["_id"].$oid

            } else {
                console.log("No company registered")
                // var companyResponse = await registerService.addCompany(data1)
                // var companyDetails = companyResponse
                // console.log(companyDetails)
                // companyId = companyDetails.data._id.$oid
            }

            // console.log(companyId)

            // var deptResponse = await registerService.addDepartment(data2)
            // var departmentDetails = deptResponse
            // console.log(departmentDetails)

            // var deptId = departmentDetails.data.departmentId

            // data1["departments"].push(deptId)

            // console.log("Update company")
            // var updateResponse = await registerService.updateCompany(data1, companyId)
            // var updateCompany = updateResponse
            // console.log(updateCompany)
            
            console.log("-------------------------------")


            // this.$router.push('/')
        },
        // check if company dept is alr registered
        // checkCompany() {

        //     var mainId = ""

        //     // CALL COMPANY MS 
        //     var url1 = 'http://localhost:5001/companyName'
        //     axios.get(url1 + "/" + this.companyName)
        //         .then(response => {

        //             this.companyFound = true
        //             mainId = response.data._id.$oid

        //             console.log(response.data)
        //         })
        //         .catch(error => {

        //             this.companyFound = false
        //             console.log("no account found")
        //             console.log(error.message)

        //         })

        //     return mainId

        // },
        // check user inputs
        checkInputs() {
            var check = true

            if (this.email == "") {
                this.errMsg.email = "Please enter an email."
                check = false
            } else {
                this.errMsg['email'] = ""
            }
            if (this.password.length < 6) {
                this.errMsg['password'] = "Please enter a password that is at least 7 characters long."
                check = false
            } else {
                this.errMsg['password'] = ""
            }
            if (this.companyDept == "") {
                this.errMsg['companyDept'] = "Please enter your company's department."
                check = false
            } else {
                this.errMsg['companyDept'] = ""
            }
            if (this.companyName == "") {
                this.errMsg['companyName'] = "Please enter your company's name."
                check = false
            } else {
                this.errMsg['companyName'] = ""
            }
            if (this.officeLocation == "") {
                this.errMsg['officeLocation'] = "Please enter your office location."
                check = false
            } else {
                this.errMsg['officeLocation'] = ""
            }

            return check
        }
    },
    components: {
        Footer
    }
}
</script>