
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
        <TopNavbar :organization="organization" :department="department"/>
        <Sidebar/>

        <div class="container-flex p-3" style="margin-left:4.5rem">
            <!-- Welcome back -->
            <div class="row px-3 pt-2 pb-4">
                <div class="col-md-7 col-sm-auto" data-aos="fade-down">
                    <h3 class="pt-3 ps-3">Welcome back,</h3>
                    <h5 class="pt-1 ps-3">&nbsp;what would you look like to do today?</h5>
                </div>
                <div class="col-md-5 col-sm-auto py-3">
                    <h4 data-aos="fade-down">Leaderboard</h4>
                    <!-- to insert link below -->
                    <small><a href="/" class="pt-3 mt-2" style="color:grey" data-aos="fade-down">View all</a></small> 
                    <div class="pt-1">
                        <table style="text-align:center">
                            <tr>
                                <th scope="col"></th>
                                <th scope="col">Department</th>
                                <th scope="col">Organisation</th>
                                <th scope="col">Points</th>
                            </tr>
                            <tr>
                            <th scope="row">1</th>
                            <td>Finance</td>
                            <td>Facebook</td>
                            <td>38</td>
                            </tr>
                            <tr>
                            <th scope="row">2</th>
                            <td>Marketing</td>
                            <td>Twitter</td>
                            <td>23</td>
                            </tr>
                            <tr>
                            <th scope="row">3</th>
                            <td>Customer Service</td>
                            <td>Apple</td>
                            <td>16</td>
                            </tr>
                            <tr>
                            <th scope="row">...</th>
                            <td>...</td>
                            <td>...</td>
                            <td>...</td>
                            </tr>
                            <tr>
                            <th scope="row">42</th>
                            <td>Finance&nbsp;<lead>(Me)</lead></td>
                            <td>Apple</td>
                            <td>4</td>
                            </tr>
                        </table>
                    </div>
                </div>
                
            </div>
            <hr>

            <!-- Shortcuts -->
            <div class="px-3 pt-2">
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
            <hr>
            
            <!-- Your listings -->
            <div class="px-3 py-2" data-aos="fade-down">
                <h3 class="ps-3">Your Listing Offers</h3>
                <small class="pt-3 ps-3 mt-2"><i>Accept or decline your offers here</i></small>
            </div>
            <div class="row pb-4" data-aos="fade-up">
                <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard>
                <ListingCard :offer="offer"></ListingCard>
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
    // import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
    // import 'bootstrap/dist/css/bootstrap.css'
    // import 'bootstrap-vue/dist/bootstrap-vue.css'
    import AOS from 'aos'
    import 'aos/dist/aos.css';


    export default {
        mounted() {
            AOS.init({
                duration: 1300,
            })
        },
        data(){
            return {
                department : "Finance",
                organization : "SMU",
                offer: true,
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
        
    }

</script>
