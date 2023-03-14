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
                <h3 class="mb-2"><i>Welcome back name,</i></h3>
                <h5>what would you look like to do today?</h5>
            </div>
            <hr>

            <!-- Explore -->
            <div class="shift">
                <h3 class="mb-2"><strong><b><i>Explore</i></b></strong></h3>
            </div>
            
            <div class="shift">
                <div class="row">
                    <div class="col-4">
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:30px; padding-right:30px;margin:0px">icon</button>
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:80px; padding-right:80px;margin:0px">
                        <lead>Listings</lead></button>
                    </div>
                    <div class="col-4">
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:30px; padding-right:30px;margin:0px">icon</button>
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:80px; padding-right:80px;margin:0px">
                        <lead>Listings</lead></button>
                    </div>
                    <div class="col-4">
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:30px; padding-right:30px;margin:0px">icon</button>
                        <button type="button" class="btn btn-outline-success" style="border-radius:0px;padding-top:30px; padding-bottom:30px; padding-left:80px; padding-right:80px;margin:0px">
                        <lead>Listings</lead></button>
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
            
            
        </div>>
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
