<template>
    <div>
        <TopNavbar />
        <Sidebar />
        <div class="container-flex p-3" style="margin-left:4.5rem;min-height:100vh">
            <div class="row px-3 py-2">
                <div class="col-lg-2">
                    <h3 class="pt-3 ps-3" data-aos="fade-down">Marketplace<span>
                        </span></h3>
                </div>
                <div data-aos="fade-down" class="col-lg-10 d-flex justify-content-lg-end justify-content-start pe-lg-4 ps-4">
                    <div>
                        
                        <ul id="growing-search-freebie" class="pt-3 mt-2 mb-0">
                            <li style="background-color:#a3a0a0;" class="rounded-3 p-1 my-0">
                                <div class="growing-search">
                                    <div class="input">
                                        <input type="text" placeholder="Enter item" v-model="search" v-on:keyup.enter="getListings()" />
                                    </div><!-- Space hack -->
                                    <div class="submit">
                                        <button type="submit" name="go_search" v-on:click="getListings()">
                                            <span class="fa fa-search"></span>
                                        </button>
                                    </div>
                                </div>
                            </li>
                        </ul>
                        <div class="form-check form-switch">
                            <div>
                                <input class="form-check-input" type="checkbox" role="switch" v-on:click="changeOption()">
                                <small>View listings from your company only</small>
                            </div>
                        </div>

                    </div>
                </div>

            </div>

            <div class="mt-3 pb-0" style="overflow: scroll;">
                <div class="d-flex justify-content-start">
                    <small class=" d-flex align-self-center pe-2 ps-3">Categories:</small>
                    <button v-for="category of categories" class="btn btn-none" v-bind:value="category" :key="category.id"
                        v-on:click="setCategory()">{{ category }}</button>
                </div>
            </div>
            <hr class="my-0">
            <div v-if="this.listedItems.length > 0" class="row py-3" data-aos="fade-up">

                <ListingCard 
                :company="item.companyName" :deptName="item.deptName" 
                :offer="offer" 
                :itemName ="item.itemName" :emission="item.carbonEmission"
                :postalCode="item.postalCode" 
                v-for="item in listedItems"></ListingCard>
                

            </div>
            <div v-else class="row py-3" data-aos="fade-up">

                <p class="text-center my-5">Sorry, no listings were found.</p>

            </div>
        </div>
    </div>
    <scroll-to-top></scroll-to-top>
        <Footer style="margin-left:4.5rem;"></Footer>
    <scroll-to-top></scroll-to-top>
</template>

<script>
import TopNavbar from "@/components/Navbar/TopNavbar.vue";
import Sidebar from "@/components/Navbar/Sidebar.vue"
import ListingCard from "@/components/ListingCard.vue"
import Footer from "@/components/Footer.vue";
import ScrollToTop from "@/components/ScrollToTop.vue";
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import itemService from "../../services/items/itemService";
import companyService from "../../services/company/companyService";
import departmentService from "../../services/department/departmentService";
import AOS from 'aos'
import 'aos/dist/aos.css';

export default {
    mounted() {
        AOS.init({
            duration: 1300,
        })

        itemService.getAllItems()
        .then((response) =>{
            console.log("Item Service Invoked")
            this.allItems = response.data;
            console.log(response.data)
            console.log(this.allItems);

            for(let i = 0; i < this.allItems.length; i++){
                if(this.allItems[i].isListed == true){

                    var temp = this.allItems[i];
                    var deptName = "";
                    var companyName = "";

                    departmentService.getDepartmentById(this.allItems[i].departmentId)
                    .then((response) => {
                        console.log(response)
                        temp["deptName"] = response.departmentName;
                        temp["postalCode"] = response.postalCode
                        console.log(deptName)
                    })
                    .catch((error) => {
                        console.log(error)
                    })

                    // temp["deptName"] = deptName;

                    companyService.getCompanyById(this.allItems[i].companyId)
                    .then((response)=>{
                        console.log(response)
                        temp["companyName"] = response.data.companyName;
                    })                    
                    .catch((error) =>{
                        console.log(error)
                    })

                    temp["companyName"] = companyName

                    this.listedItems.push(temp)
                }
            }

            console.log(this.listedItems)
        })
        .catch((error)=>{
            console.log(error)
        })

        this.checkuser()

        this.deptId = sessionStorage.getItem("deptId")
        this.companyId = sessionStorage.getItem("companyId")
    },
    data() {
        return {
            deptId: '',
            allItems : undefined,
            listedItems: [],
            company: "SMU",
            department: "Finance",
            search: "",
            offer: false,
            outsideCompany: true,
            allListings: [],
            gotListings: true
        }
    },
    components: {
        TopNavbar,
        Sidebar,
        ListingCard,
        Footer,
        ScrollToTop
    },
    methods: {
        changeOption(){
            if (this.outsideCompany){
                this.outsideCompany = false
            } else {
                this.outsideCompany = true
            }
            this.getListings()
        },
        getListings() {
            var all = true
            this.gotListings = true
            this.allListings = []

            if (this.search != ""){
                all = false
            }

            var url = "http://localhost:3004/"

            axios.get(url)
            .then(response => {

                console.log(response.data)

                var listings = response.data

                // View within company only
                if (!this.outsideCompany){

                    listings = []

                    for (let each of listings){
                        if (each.companyId == this.companyId){
                            listings.push(each)
                        }
                    }
                }

                // search for items in the marketplace

                // Search not empty
                if (this.search != ""){
                    var temp = []

                    for (let each of listings){
                        if (each.itemName.toLowerCase() == this.search.toLowerCase()){
                            temp.push(each)
                        }
                    }

                    listings = temp

                    this.search = ""
                }

                this.allListings = listings

                if (this.allListings.length == 0){
                    this.gotListings = false
                } else {
                    this.gotListings = true
                }


            })
            .catch(error => {

                console.log(error.message)
                
            })
        },
        checkuser(){
            const auth = getAuth();
            onAuthStateChanged(auth, (user) => {
                if (!user) {
                    console.log('user is not logged in')
                    window.location.href = `/`;
                }
            });
        },
    }

}

</script>
