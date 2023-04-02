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

            <hr class="mb-0">
            <div v-if="gotListings" class="row py-3" data-aos="fade-up">

                <ListingCard :offer="offer" v-for="each of allListings" :listingInfo="each"></ListingCard>

            </div>
            <div v-else class="row py-3" data-aos="fade-up">

                <small class="text-center my-5">Sorry, no listings were found.</small>

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
import AOS from 'aos'
import 'aos/dist/aos.css';

import { getAuth, onAuthStateChanged} from "firebase/auth";

export default {
    mounted() {
        AOS.init({
            duration: 1300,
        })
        this.getListings()
        this.checkuser()

        this.deptId = sessionStorage.getItem("deptId")
        this.companyId = sessionStorage.getItem("companyId")
        this.deptName = sessionStorage.getItem("deptName")
        this.companyName = sessionStorage.getItem("companyName")
    },
    data() {
        return {
            deptId: '',
            companyId: '',
            deptName: '',
            companyName: '',
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

                // Search for items in the marketplace
                var listed = []
                for (let each of listings){
                    if (each.isListed){
                        listed.push(each)
                    }
                }
                listings = listed

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
                console.log(this.allListings)

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
