<script>

</script>

<template>
  <div v-if="offer" class="col-xl-3 col-md-6 py-4 d-flex justify-content-center">
    <div class="card p-1">
        <img src="https://i.postimg.cc/1X8R7m8y/design.png"/>
        <div class="p-2">
            <div class="d-flex justify-content-between align-items-center">
                <p style="font-size:20px" class="desc">{{itemName}}</p>
                <small class="desc"><i class="fa-solid fa-smog"></i> {{emission}}</small>
            </div>
            <i class="fa-solid fa-location-dot" style="color:#a3a0a0"><span class="desc ps-1">{{address}}</span></i>
            <i class="fa-solid fa-building d-block" style="color:#a3a0a0"><span class="desc ps-1">{{company}}, {{department}}</span></i>
        </div>
        <div class="card__content">
            <div class="d-flex justify-content-center mt-2">
              <button class="btn btn-light desc" v-on:click="acceptOffer"><span>Accept</span></button>
              <button class="btn btn-dark desc" v-on:click="declineOffer"><span>Decline</span></button>
            </div>
          </div>

      </div>
  </div>

  <div v-else class="col-xl-3 col-md-6 py-4 d-flex justify-content-center">
    <div class="card p-1">
        <img src="https://i.postimg.cc/1X8R7m8y/design.png"/>
        <div class="p-2">
            <div class="d-flex justify-content-between align-items-center">
                <p style="font-size:20px" class="desc">{{itemName}}</p>
                <small class="desc"><i class="fa-solid fa-smog"></i> {{emission}}</small>
            </div>
            <i class="fa-solid fa-location-dot" style="color:#a3a0a0"><span class="desc ps-1">{{address}}</span></i>
            <i class="fa-solid fa-building d-block" style="color:#a3a0a0"><span class="desc ps-1">{{company}}, {{department}}</span></i>
        </div>

        <div class="card__content">
            <div class="d-flex justify-content-center mt-2">
              <button class="btn btn-light desc" v-on:click="viewMore"><span>View More</span></button>
            </div>
          </div>
      </div>
  </div>
</template>

<script>

export default {
    data(){
        return {
            itemName: "IKEA Chair",
            address: "Bras Basah",
            company: "SMU",
            department: "Finance",
            emission: "500",
            img: "",
            listingId: 1
        }
    },
    props: ["listingId", "offer"],
    methods: {

        // OFFER FUNCTIONS
        acceptOffer(){
            console.log("accept offer")
        },
        declineOffer(){
            console.log("decline offer")
        },

        // LISTING FUNCTIONS
        viewMore(){
            console.log("view more")

            // set session variable to view listing
            sessionStorage.setItem("viewListing", this.listingId);

            // re-route to listing page
            this.$router.push({path: '/listing'});
        },

        getListing() {
            var url = ""

            axios.get(url, {
                params: {
                    listingId: this.listingId
                }
            })
            .then(response => {

                this.itemName = "IKEA Chair",
                this.address = "Bras Basah", // might have to use geolocation to retrieve this
                this.company = "SMU",
                this.department = "Finance",
                this.emission = "500",
                this.img = ""
                
            })
            .catch(error => {

                console.log(error.message)
                
            })
        }
    }
}

</script>

<style>
    .desc {
        font-family: 'Nunito Sans';
        max-height: 100px;
        overflow: scroll;
    }
    .card{
    height: 400px;
    width:280px;
    cursor:pointer;
    background-color:#fff;
    }
    .card img{
    width:100%;
    height:300px;
    border-radius:10px;
    position:relative;
    z-index:1;
    transition:all .5s ease-in-out;
    }
    .card__content{
    margin:1rem 0;
    color:#222;
    overflow:hidden;
    margin-top:-67px;
    opacity:0;
    visibility:hidden;
    transition:all .5s ease-in-out;
    }
    .card:hover img{
    margin-top:-20px;
    box-shadow:0 0 4px 6px rgba(99, 99, 99, 0.3);
    }
    .card:hover>.card__content{
    margin-top:0;
    opacity:1;
    visibility:visible;
    }
    @media screen and (max-width:800px){
    .container{
        flex-wrap:wrap;
    }
    }

</style>