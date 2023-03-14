<template>
    <TopNavbar></TopNavbar>
    <Sidebar></Sidebar>
    <div class="row ps-5">
        <router-link to="/marketplace" class="pt-4 ps-5"><i class="fa-solid fa-arrow-left-long ps-5"
                style="color:#6e9190;height: 20px;"> <span style="font-style:italic;"> Back to
                    Marketplace</span></i></router-link>
    </div>

    <div class="row ps-3 py-4 pe-4" style="margin-left:4.5rem;">

        <div class="col-xl-6">

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

        <div class="col-xl-6 pe-5 text-start mt-xl-0 mt-5 pt-xl-0 pt-3">

            <div class="row d-flex justify-content-between">

                <div class="col-xl-8">
                    <h4>IKEA Chair</h4>
                </div>
                <div class="col-xl-4 text-xl-end text-start">
                    <small class="desc">{{status}}</small>
                </div>

            </div>
            <i class="fa-solid fa-location-dot mt-1" style="color:#a3a0a0"><span class="desc ps-1">{{address}}</span></i>
            <i class="fa-solid fa-building d-block mt-1" style="color:#a3a0a0"><span class="desc ps-1">{{company}}, {{department}}</span></i>
            <hr>

            <p style="font-style:italic;font-weight:bold;">Description:</p>
            <div style="overflow:scroll; height: 400px;" class="mt-2">
                <p>{{desc}} Lorem ipsum, dolor sit amet consectetur adipisicing elit. Totam cum quos repudiandae iure exercitationem repellat expedita quia facere? Beatae asperiores harum amet quae provident alias repellendus dolorem? Voluptatibus, nemo quos? Lorem ipsum dolor sit amet consectetur adipisicing elit. Odit sequi fugit nulla, aliquam necessitatibus pariatur in veritatis enim suscipit soluta optio, quas voluptas dolorem, nam sint dolore molestias incidunt facere. Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat modi maiores cum repellendus dolor, possimus temporibus tempore nam. Dolor sed magnam accusamus soluta beatae quas at. Fugiat, quidem architecto? Et. Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit, rem. Enim nesciunt quam obcaecati dignissimos sapiente rerum, ipsa, magnam ipsum laborum, molestias est. Repellendus dicta provident cum velit modi ratione! Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur, libero fuga. At magni similique quidem quod optio, culpa iure, a earum hic quasi excepturi delectus saepe ratione. Amet, numquam libero. Lorem ipsum, dolor sit amet consectetur adipisicing elit. At quisquam aspernatur, incidunt maiores fuga perferendis illo quis illum consequuntur laborum reiciendis minus saepe sint rem autem! Error blanditiis sapiente dolorum?</p>
            </div>

            <div class="d-flex justify-content-center my-3">
                <button class="btn btn-light text-center"><span><i class="fa-regular fa-comment" style="color:#6e9190">
                </i> &nbsp; Contact Seller</span></button>
            </div>


        </div>





    </div>
</template>

<script>
import TopNavbar from "@/components/Navbar/TopNavbar.vue";
import Sidebar from "@/components/Navbar/Sidebar.vue"
import ListingCard from "@/components/ListingCard.vue"

export default {
    data() {
        return {
            search: "",
            header: "Marketplace",
            categories: ["Furniture", "Office Supplies", "Equipment", "Electronics", "IT",
                "Lightings", "Decor", "Kitchen", "Others"],
            category: "",
            itemName: "IKEA Chair",
            address: "Bras Basah",
            company: "SMU",
            department: "Finance",
            desc: "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.",
            status: "Used",
            img: ""
        }
    },
    components: {
        TopNavbar,
        Sidebar,
        ListingCard
    },
    methods: {
        setCategory() {
            console.log(event.target.value)
            this.category = event.target.value
            this.header = "Marketplace,"
        }
    }

}

</script>

<style>
.carousel-item img {
    height: 650px;
    width: 650px;
    object-fit: cover;
}
</style>