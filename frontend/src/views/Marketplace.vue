<template>
    <TopNavbar/>
    <Sidebar/>
    <div class="container-flex" style="margin-left:4.5rem">
        <div class="row">
            <div class="col-lg-2">
                <h3 class="pt-3 ps-3 mt-2">Marketplace, <span><h4>Furniture</h4></span></h3>
            </div>
            <div class="col-lg-10 d-flex justify-content-lg-end justify-content-start pe-lg-4 ps-4">
                <div>
                    <ul id="growing-search-freebie" class="pt-3 mt-2 mb-0">
                        <li style="background-color:#c5dad2;" class="rounded-3 p-1 my-0">
                        <div class="growing-search">
                            <div class="input">
                            <input type="text" placeholder="Enter item" v-model="search"/>
                            </div><!-- Space hack --><div class="submit">
                            <button type="submit" name="go_search">
                                <span class="fa fa-search"></span>
                            </button>
                            </div>
                        </div>
                        </li>
                    </ul>
                    <div class="form-check form-switch">
                        <div class="">
                            <input class="form-check-input" type="checkbox" role="switch">
                            <small>Include other organisations</small>
                        </div>
                    </div>

                </div>
            </div>

        </div>

        <div class="row mt-3 pb-0">
            <div class="col-2 d-flex align-items-center">
                <small class="ps-3">Categories:</small>
            </div>
            <div class="col-10" style="overflow: scroll;">
                <div class="d-flex justify-content-center">
                    <button v-for="category of categories" class="btn btn-none">{{category}}</button>
                </div>

            </div>
        </div>
        <hr class="my-0">

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
</template>

<script>
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue"
    import ListingCard from "@/components/ListingCard.vue"

    export default {
        data(){
            return {
                search: "",
                categories: ["Furniture", "Office Supplies", "Equipment", "Electronics", "IT", 
                            "Lightings", "Decor", "Kitchen", "Others"]
            }
        },
        components: {
            TopNavbar,
            Sidebar,
            ListingCard
        }
        
    }

</script>
