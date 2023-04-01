<template>
    <TopNavbar></TopNavbar>
    <Sidebar></Sidebar>
    <div class="row ps-5">
        <router-link to="/marketplace" class="pt-4 ps-5"><i class="fa-solid fa-arrow-left-long ps-5"
                style="color:#6e9190;height: 20px;"> <span style="font-style:italic;"> Back to
                    Marketplace</span></i></router-link>
    </div>
    <div class="row ps-5 py-4 pe-4" style="margin-left:4.5rem;" data-aos="fade-down">

        <div class="col-xl-6 pb-5">

            <!-- Carousel wrapper -->
            <div id="carouselExampleIndicators" class="carousel slide carousel-fade" data-ride="carousel"
                style="height:100%;width:auto;">
                <!-- Slides -->
                <div class="carousel-inner mb-5">
                    <div class="carousel-item active d-flex justify-content-center">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(88).webp" class="d-block" alt="..." />
                    </div>
                    <div class="carousel-item d-flex justify-content-center">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(121).webp" class="d-block" alt="..." />
                    </div>
                    <div class="carousel-item d-flex justify-content-center">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/Slides/img%20(31).webp" class="d-block" alt="..." />
                    </div>
                </div>
                <!-- Slides -->

                <!-- Controls -->
                <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
                    data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
                    data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
                <!-- Controls -->

                <!-- Thumbnails -->
                <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
                        aria-current="true" aria-label="Slide 1" style="width: 50px;">
                        <img class="d-block w-100 img-fluid" style="height:50px;object-fit:cover;"
                            src="https://mdbcdn.b-cdn.net/img/Photos/Others/Carousel-thumbs/img%20(88).webp" />
                    </button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                        aria-label="Slide 2" style="width: 50px;">
                        <img class="d-block w-100 img-fluid" style="height:50px;object-fit:cover;"
                            src="https://mdbcdn.b-cdn.net/img/Photos/Others/Carousel-thumbs/img%20(121).webp" />
                    </button>
                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
                        aria-label="Slide 3" style="width: 50px;">
                        <img class="d-block w-100 img-fluid" style="height:50px;object-fit:cover;"
                            src="https://mdbcdn.b-cdn.net/img/Photos/Others/Carousel-thumbs/img%20(31).webp" />
                    </button>
                </div>
                <!-- Thumbnails -->
            </div>
            <!-- Carousel wrapper -->

        </div>

        <div class="col-xl-6 pe-5 ps-4 text-start mt-xl-0 mt-5 pt-xl-0 py-2">

            <div class="d-flex justify-content-between">
                <div class="">
                    <h4>{{ itemName }}</h4>
                </div>
                <div class="">
                    <p class="desc" style="color:#a3a0a0"> {{ emission }} <i class="fa-solid fa-smog"></i></p>
                </div>

            </div>
            <i class="fa-solid fa-building d-block mt-1" style="color:#a3a0a0"><span class="desc ps-1">{{ company }}, {{
                department }}</span></i>
            <hr>

            <div class="d-flex justify-content-between align-items-center">

                <p style="font-style:italic;font-weight:bold;">Description:</p>
                <div>
                    <button v-if="sent" class="btn btn-dark text-center" disabled><span><i class="fa-solid fa-paper-plane" style="color:#c5dad2"></i> &nbsp; Offer Sent</span></button>
                    <button v-else class="btn btn-dark text-center" v-on:click="sendOffer()"><span><i class="fa-solid fa-paper-plane" style="color:#c5dad2"></i> &nbsp; Send Offer</span></button>

                    <button class="btn btn-light text-center"><span><i class="fa-regular fa-comment" style="color:#6e9190" v-on:click="contactSeller">
                            </i> &nbsp; Contact Seller</span></button>
                </div>
            </div>

            <div class="mt-4">
                <p>{{ desc }}</p>
            </div>

            <!-- <div class="d-flex justify-content-center mt-3 mb-4">
                <button class="btn btn-light text-center"><span><i class="fa-regular fa-comment" style="color:#6e9190">
                        </i> &nbsp; Contact Seller</span></button>
            </div> -->

        </div>
    </div>
    <Footer style="margin-left:4.5rem;"></Footer>
</template>

<script>
import TopNavbar from "@/components/Navbar/TopNavbar.vue";
import Sidebar from "@/components/Navbar/Sidebar.vue"
import ListingCard from "@/components/ListingCard.vue"
import Footer from "@/components/Footer.vue"
import AOS from 'aos'
import 'aos/dist/aos.css';

import { getAuth, onAuthStateChanged} from "firebase/auth";

export default {
    mounted() {
        AOS.init({
            duration: 1300,
        })
        this.checkuser()

        this.deptId = sessionStorage.getItem("deptId")

        this.listingInfo = JSON.parse(sessionStorage.getItem("viewListing"));
        console.log(this.listingInfo)

        this.listingId = this.listingInfo._id
        this.itemName = this.listingInfo.itemName
        this.company = this.listingInfo.company.companyName 
        this.department = this.listingInfo.department.departmentName 
        this.emission =  this.listingInfo.carbonEmission
        this.img = this.listingInfo.itemPicture
        this.desc = this.listingInfo.itemDescription

    },
    data() {
        return {
            sent: false,

            listingInfo: "",
            itemName: "",
            company: "",
            department: "",
            desc: "",
            emission: "",
            img: "",

            creatorId: "",
            deptId: ""

        }
    },
    components: {
        TopNavbar,
        Sidebar,
        ListingCard,
        Footer
    },
    methods: {
        sendOffer(){
            console.log("offer sent")
            this.sent = true
        },
        contactSeller(){

        },
        getListing(){

            this.listingId = this.listingInfo._id
            this.itemName = this.listingInfo.itemName
            this.company = this.listingInfo.company.companyName 
            this.department = this.listingInfo.department.departmentName 
            this.emission =  this.listingInfo.carbonEmission
            this.img = this.listingInfo.itemPicture
            this.desc = this.listingInfo.itemDescription


            // console.log(this.listingId);

            // axios.get(url, {
            //     params: {
            //         listingId: this.listingId
            //     }
            // })
            // .then(response => {
            //     // retrieve item details + creatorId

            //     this.itemName = "IKEA Chair",
            //     this.company = "SMU",
            //     this.department = "Finance",
            //     this.emission = "500",
            //     this.img = ""
                
            // })
            // .catch(error => {

            //     console.log(error.message)
                
            //     })
        
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
        
    },
    // beforeMount() {
    //     this.listingInfo = sessionStorage.getItem("viewListing");
    //     console.log(this.listingInfo)

    //     // this.listingId = this.listingInfo._id
    //     // this.itemName = this.listingInfo.itemName
    //     // this.company = this.listingInfo.company.companyName 
    //     // this.department = this.listingInfo.department.departmentName 
    //     // this.emission =  this.listingInfo.carbonEmission
    //     // this.img = this.listingInfo.itemPicture
    //     // this.desc = this.listingInfo.itemDescription

    //     // this.getListing()
    // },
        


}

</script>

<style>
.carousel-item img {
    height: 650px;
    width: 650px;
    object-fit: cover;
}</style>