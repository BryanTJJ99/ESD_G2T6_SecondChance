<template>
    <TopNavbar/>
    <Sidebar/>
    <div class="container-flex" style="margin-left:4.5rem">
        <div class="row px-3 py-2">
            <div class="col-lg-2">
                <h3 class="pt-3 ps-3 mt-2">{{header}} <span><h4>{{category}}</h4></span></h3>
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
                        <div>
                            <input class="form-check-input" type="checkbox" role="switch">
                            <small>Include other organisations</small>
                        </div>
                    </div>

                </div>
            </div>

        </div>

        <div class="mt-3 pb-0 ps-3" style="overflow: scroll;">
            <div class="d-flex justify-content-start">
                <small class=" d-flex align-self-center pe-2 ps-3">Categories:</small>
                <button v-for="category of categories" class="btn btn-none" v-bind:value="category" v-on:click="setCategory()">{{category}}</button>
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
                company: "SMU",
                department: "Finance",
                search: "",
                header: "Marketplace",
                categories: ["Furniture", "Office Supplies", "Equipment", "Electronics", "IT", 
                            "Lightings", "Decor", "Kitchen", "Others"],
                category: ""
            }
        },
        components: {
            TopNavbar,
            Sidebar,
            ListingCard
        },
        methods: {
            setCategory(){
                console.log(event.target.value)
                this.category = event.target.value
                this.header = "Marketplace,"
            }
        }
        
    }

</script>
