<style>

table {
    border-collapse:separate;
    border:solid black 1px;
    border-radius:6px;
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
            <div class="row px-3 py-2">
                <div class="col-md-7 col-sm-auto">
                    <!-- <h3 class="mb-2"><i>Welcome back name,</i></h3> -->
                    <h3 class="pt-3 ps-3 mt-2">Welcome back name,</h3>
                    <h5 class="pt-1 ps-3">&nbsp;what would you look like to do today?</h5>
                </div>
                <div class="col-md-5 col-sm-auto pt-3 ps-3">
                    <h4 class="pt-3 ps-3">Leaderboard</h4>
                    <spacer></spacer>
                    <!-- to insert link below -->
                    <small><a href="/" class="pt-3 ps-3 mt-2" style="color:grey">View all</a></small> 
                    <div class="pt-3 ps-3" style="margin-right:25px">
                        <table class="table border rounded" style="text-align:center">
                            <thead>
                                <tr>
                                <th scope="col"></th>
                                <th scope="col"></th>
                                <th scope="col">Department</th>
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
                                <td>38</td>
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
                                <td>Apple</td>
                                <td>16</td>
                                </tr>
                                <tr>
                                <th scope="row">...</th>
                                <td>...</td>
                                <td>...</td>
                                <td>...</td>
                                <td>...</td>
                                </tr>
                                <tr>
                                <th scope="row">42</th>
                                <td><img src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/img (9).webp" class="rounded-circle"
                                height="36" alt="Avatar" loading="lazy" /></td>
                                <td>Doge&nbsp;<lead>(Me)</lead></td>
                                <td>Apple</td>
                                <td>4</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <hr>

            <!-- Shortcuts -->
            <div class="px-3 pt-2">
                <h3 class="mb-2">Shortcuts</h3>
            </div>
            
            <div class="shift d-flex-center px-3 py-2">
                <div class="row  pt-3 ps-3 mt-2">
                    <div class="col col-sm-auto pb-4">
                        <button type="button" class="btn btn-outline-success" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px">
                            <img src="../assets/clipboard.png" height="81" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>Add New Listing</lead></button>
                    </div>
                    <div class="col col-sm-auto">
                        <button type="button" class="btn btn-outline-dark" style="border-radius:10px 0px 0px 10px;padding:0px; margin:0px">
                            <img src="../assets/dchair.png" height="82" style="margin:0px;padding:10px">
                        </button>
                        <button type="button" class="btn" style="border-radius:0px 10px 10px 0px;padding-top:30px; padding-bottom:30px;margin:0px;border-color:#c5dad2" disabled>
                        <lead>&nbsp;Add New Inventory&nbsp;</lead></button>
                    </div>
                </div>
            </div>
            <hr>
            
            <!-- Your listings -->
            <div class="px-3 py-2">
                <h3 class="pt-3 ps-3 mt-2"><strong><b><i>Your Listings</i></b></strong></h3>
                <small class="pt-3 ps-3 mt-2"><i>Listed by your department</i></small>
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
