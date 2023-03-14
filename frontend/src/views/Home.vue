<style>
.shift{
    margin-left: 1.5rem;
    margin-top: 1rem;
}


</style>
<template>
    <div>
        <TopNavbar :organization="organization" :department="department"/>
        <Sidebar/>
        <Footer/>

        <div class="container-flex" style="margin-left:4.5rem">
            <!-- Welcome back -->
            <div class="shift">
                <div class="row">
                    <div class="col-sm-7">
                        <h3 class="mb-2"><i>Welcome back name,</i></h3>
                        <h5>what would you look like to do today?</h5>
                    </div>
                    <div class="col-sm-5">
                        <h4>Leaderboard</h4>
                        <spacer></spacer>
                        <!-- to insert link below -->
                        <small><a href="/" style="color:grey">View all</a></small> 
                        <div class="container">
                            <table class="table" style="border:1px solid green; margin-right:30px">
                                <thead>
                                  <tr>
                                    <th scope="col"></th>
                                    <th scope="col"></th>
                                    <th scope="col">Name</th>
                                    <th scope="col">Organisation</th>
                                    <th scope="col">Points</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  <tr>
                                    <th scope="row">1</th>
                                    <td><img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (31).webp" class="rounded-circle"
                                        height="36" alt="Avatar" loading="lazy" /></td>
                                    <td>Otto</td>
                                    <td>Facebook</td>
                                    <td>3</td>
                                  </tr>
                                  <tr>
                                    <th scope="row">2</th>
                                    <td><img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (25).webp" class="rounded-circle"
                                    height="36" alt="Avatar" loading="lazy" /></td>
                                    <td>Thornton</td>
                                    <td>Twitter</td>
                                    <td>23</td>
                                  </tr>
                                  <tr>
                                    <th scope="row">3</th>
                                    <td><img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (12).webp" class="rounded-circle"
                                    height="36" alt="Avatar" loading="lazy" /></td>
                                    <td>Human</td>
                                    <td>Appler</td>
                                    <td>16</td>
                                  </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <hr>

            <!-- Explore -->
            <div class="shift">
                <h3 class="mb-2"><strong><b><i>Explore</i></b></strong></h3>
            </div>
            
            <div class="shift d-flex-center">
                <div class="row">
                    <!-- <div class="col col-md-auto">
                        <button type="button" class="btn btn-light">
                        <i class="larger fas fa-list" style="color:black"></i>&nbsp;&nbsp;&nbsp;&nbsp;<lead>Add Listing</lead></button>
                    </div>
                    <div class="col-md-auto">
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:83px; padding-right:83px;margin:0px">
                        <i class="larger fas fa-truck-moving" style="color:black"></i>&nbsp;&nbsp;&nbsp;&nbsp;<lead>Add Asset</lead></button>
                    </div> -->
                    <div class="col col-md-auto">
                        <button type="button" class="btn btn-outline-success" style="border-radius:10px 0px 0px 10px;padding-top:30px; padding-bottom:30px; padding-left:30px; padding-right:30px;margin:0px">
                            <i class="larger fas fa-home" style="color:black"></i>
                        </button>
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px; padding-left:74px; padding-right:74px;margin:0px">
                        <lead>Add Listing</lead></button>
                    </div>
                    <div class="col col-md-auto">
                        <button type="button" class="btn btn-outline-success" style="border-radius:10px 0px 0px 10px;padding-top:30px; padding-bottom:30px; padding-left:30px; padding-right:30px;margin:0px">
                            <i class="larger fas fa-home" style="color:black"></i>
                        </button>
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px; padding-left:74px; padding-right:74px;margin:0px">
                        <lead>Add Asset</lead></button>
                    </div>
                </div>
            </div>
            <hr>
            
            <!-- Your listings -->
            <div class="shift">
                <h3><strong><b><i>Your Listings</i></b></strong></h3>
                <small><i>Listed by your department</i></small>
            </div>
            <div class="row">
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
            </div>
        </div>
    </div>


</template>

<script>
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue";
    import Footer from "@/components/Footer.vue";
    import ListingCard from "@/components/ListingCard.vue";

    export default {
        data(){
            return {
                department : "Finance",
                organization : "SMU",
            }
        },
        components: {
            TopNavbar,
            Sidebar,
            Footer,
            ListingCard
        },
        
    }

</script>
