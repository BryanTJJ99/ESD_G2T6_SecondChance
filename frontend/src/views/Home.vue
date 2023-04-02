
<style>
table {
    border-collapse: collapse;
    width: 100%;
    max-width: 740px;
    margin: 0 auto;
    border-radius: 10px;
    overflow: hidden;
  }
  
  th, td {
    text-align: center;
    padding: 10px;
    background-color: #f2f6f5f0;
  }
  
  th {
    background-color: #f2f6f5f0;
    font-weight: bold;
  }

</style>
<template>
    <div>
        <TopNavbar/>
        <Sidebar/>

        <div class="container-flex p-3" style="margin-left:4.5rem; height:100vh">
            <!-- Welcome back -->
            <div class="row px-3 pt-2 pb-4">
                <div class="col-md-7 col-sm-auto" data-aos="fade-down">
                    <h3 class="pt-3 ps-3">Welcome back, {{organization}} {{department}}</h3>
                    <h5 class="pt-1 ps-3">&nbsp;what would you look like to do today?</h5>
                </div>
                <div class="col-md-5 col-sm-auto py-3" data-aos="fade-down">
                    <h4 data-aos="fade-down">Leaderboard</h4>
                    <div class="pt-1">
                        <table style="text-align:center">
                            <tr>
                                <th scope="col"></th>
                                <th scope="col">Department</th>
                                <th scope="col">Organisation</th>
                                <th scope="col">Points</th>
                            </tr>
                            <tr v-for="dept,index in myCompany">
                                <th scope="col">{{ index }}</th>
                                <th scope="col">{{dept.departmentName}}</th>
                                <th scope="col">{{this.companyName}}</th>
                                <th scope="col">{{ dept.totalCarbon }}</th>
                            </tr>
                            
                        </table>
                    </div>
                </div>
                
            </div>
            <hr>

            <!-- Shortcuts -->
            <!-- <div class="px-3 pt-2">
                <h3 class=" ps-3 mb-2" data-aos="fade-down">Shortcuts</h3>
            </div>
            
            <div class="shift d-flex-center ps-3">
                <div class="row pt-3 ps-3 mt-2">
                    <div class="col col-sm-auto pb-4">
                        <button type="button" class="btn btn-dark" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px">
                            <img src="../assets/clipboard.png" height="81" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>Add a New Listing</lead></button>
                    </div>
                    <div class="col col-sm-auto">
                        <button type="button" class="btn btn-dark" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px">
                            <img src="../assets/dchair.png" height="82" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>Add a New Inventory</lead></button>
                    </div>
                </div>
            </div>
            <hr> -->
            
            <!-- Your listings -->
            <div class="px-3 py-2" data-aos="fade-down">
                <h3 class="ps-3">Your Listing Offers</h3>
                <small class="pt-3 ps-3 mt-2"><i>Accept or decline your offers here</i></small>
            </div>
            <div class="row pb-4" data-aos="fade-up">
                <!-- <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard> -->
            </div>
        </div>
     
        <scroll-to-top></scroll-to-top>
        <Footer style="margin-left:4.5rem;"></Footer>

    </div>


</template>

<script>
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue";
    import Footer from "@/components/Footer.vue";
    import ListingCard from "@/components/ListingCard.vue";
    import ScrollToTop from "@/components/ScrollToTop.vue"
    import itemDetailsService from "../../services/item_details/itemDetailsService";
    import AOS from 'aos'
    import 'aos/dist/aos.css';

    import { getAuth, onAuthStateChanged} from "firebase/auth";
import { computed } from "@vue/reactivity";
import departmentService from "../../services/department/departmentService";

    export default {
        mounted() {
            AOS.init({
                duration: 1300,
            })
            
            this.checkuser()

            this.deptId = sessionStorage.getItem("deptId")
            this.deptName = sessionStorage.getItem("deptName")
            this.companyId = sessionStorage.getItem("companyId")
            this.companyName = sessionStorage.getItem("companyName")

            this.getOffers()
            this.leaderBoard()

            
        },
        data(){
            return {
                myCompany: [],
                offers : undefined,
                deptName : "",
                companyName : "",
                deptId: "",
                companyId: "",
                offer: true,
                deptId: '',
                name: ''
            }
        },
        components: {
            TopNavbar,
            Sidebar,
            Footer,
            ListingCard,
            ScrollToTop
            // BootstrapVue
        },
        methods: {
            checkuser(){
                const auth = getAuth();
                onAuthStateChanged(auth, (user) => {
                    if (!user) {
                        console.log('user is not logged in')
                        window.location.href = `/`;
                    }
                });
            },

            getOffers: async function(){
                var offers = await itemDetailsService.getDepartmentOffers(this.deptId)
                var complexOffers = offers;

                this.offers = complexOffers.data
                console.log(this.offers)
            },


            leaderBoard: async function(){
                var alldepts = await departmentService.getAllDepartments()
                console.log("COMPANY ID")
                console.log(this.companyId)
                console.log("ALL COMPANY")
                console.log(alldepts)

                
                for(var dept of alldepts){
                    if (dept['companyId'] == this.companyId){
                        this.myCompany.push(dept)
                        console.log("PUSHED")
                    }
                }
                console.log("BEFORE SORT")
                console.log(this.myCompany)


                this.myCompany.sort((a,b)=>{
                    return b.totalCarbon - a.totalCarbon
                })
                
                if (this.myCompany.length > 5){
                    this.myCompany = this.myCompany.slice(4)
                }
            }
        },
    }

</script>
