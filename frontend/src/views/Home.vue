<style>
.shift{
    margin-left: 1.5rem;
    margin-top: 1rem;
}

td {
    padding-top: 10px;
    padding-bottom: 10px;
}


</style>
<template>
    <div>
        <TopNavbar :organization="organization" :department="department"/>
        <Sidebar/>

        <div class="container-flex p-3" style="margin-left:4.5rem">
            <!-- Welcome back -->
            <div class="">
                <div class="row px-3 py-2">
                    <div class="col-sm-7">
                        <h3 class="mb-2"><i>Welcome back,</i></h3>
                        <h5>what would you look like to do today?</h5>
                    </div>
                    <div class="col-sm-5">
                        <h4>Leaderboard</h4>
                        <spacer></spacer>
                        <!-- to insert link below -->
                        <small><a href="/" style="color:grey">View all</a></small> 
                        <div class="mt-1">
                            <table class="table border rounded" style="text-align:center">
                                <thead>
                                    <tr>
                                    <th scope="col"></th>
                                    <th scope="col">Department</th>
                                    <th scope="col">Organisation</th>
                                    <th scope="col">Points</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                    <th scope="row">1</th>
                                    <td>Otto</td>
                                    <td>Facebook</td>
                                    <td>38</td>
                                    </tr>
                                    <tr>
                                    <th scope="row">2</th>
                                    <td>Thornton</td>
                                    <td>Twitter</td>
                                    <td>23</td>
                                    </tr>
                                    <tr>
                                    <th scope="row">3</th>
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

            <!-- Shortcuts -->
            <div class="px-3 pt-2">
                <h3 class="mb-2">Shortcuts</h3>
            </div>
            
            <div class="shift d-flex-center pb-2">
                <div class="row">
                    <!-- <div class="col col-md-auto">
                        <button type="button" class="btn btn-light">
                        <i class="larger fas fa-list" style="color:black"></i>&nbsp;&nbsp;&nbsp;&nbsp;<lead>Add Listing</lead></button>
                    </div>
                    <div class="col-md-auto">
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:83px; padding-right:83px;margin:0px">
                        <i class="larger fas fa-truck-moving" style="color:black"></i>&nbsp;&nbsp;&nbsp;&nbsp;<lead>Add Asset</lead></button>
                    </div> -->
                    <div class="col col-sm-auto">
                        <button type="button" class="btn btn-dark" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px;border-color:#c5dad2">
                            <img src="../assets/clipboard.png" height="82" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>Add New Listing</lead></button>
                    </div>
                    <div class="col col-sm-auto">
                        <button type="button" class="btn btn-dark" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px;border-color:#c5dad2">
                            <img src="../assets/dchair.png" height="82" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>&nbsp;Add New Inventory&nbsp;</lead></button>
                    </div>
                </div>
            </div>
            <hr>
            
            <!-- Your listings -->
            <div class="px-3 pt-2">
                <h3>Your Recent Listings</h3>
                <small><i>Listed by your department</i></small>
            </div>
            <div class="row">
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
                <ListingCard></ListingCard>
            </div>
        </div>
        <Footer></Footer>
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
