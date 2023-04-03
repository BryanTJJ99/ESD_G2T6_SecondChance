<script>

</script>

<template>
  <div v-if="offer" class="col-xl-3 col-md-6 py-4 d-flex justify-content-center">
    <div class="card p-1">

        <!--Image Select-->
        <img v-if="listingInfo['itemCategory'] == 'Furniture'" src="https://res.cloudinary.com/castlery/image/private/w_1000,f_auto,q_auto/b_rgb:F3F3F3,c_fit/v1624964497/crusader/variants/40550131/Seb-Desk-Lifestyle-Crop.jpg" alt="">

        <img v-else-if="listingInfo['itemCategory'] == 'Electronics'" src="https://www.tds-office.com/wp-content/uploads/2018/10/office-electronics-printers-copiers.jpg" alt="">
        
        <img v-else-if="listingInfo['itemCategory'] == 'Office Supplies'" src="https://storables.com/wp-content/uploads/2020/06/AdobeStock_221435829-1024x684.jpeg" alt="">

        <img v-else src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png"/>


        <div class="p-2">
            <div class="d-flex justify-content-between align-items-center">
                <p style="font-size:20px" class="desc">{{itemName}}</p>
                <small class="desc"><i class="fa-solid fa-smog"></i> {{emission}}</small>
            </div>
            <i class="fa-solid fa-building d-block" style="color:#a3a0a0"><span class="desc ps-1">{{company}}, {{department}}</span></i>
        </div>
        <div class="card__content">
            <div class="d-flex justify-content-center mt-2">
              <button class="btn btn-light desc" v-on:click="acceptOffer"><span>Accept</span></button>
            </div>
          </div>

      </div>
  </div>

  <div v-else class="col-xl-3 col-md-6 py-4 d-flex justify-content-center">
    <div class="card p-1">

        <img v-if="listingInfo['itemCategory'] == 'Furniture'" src="https://res.cloudinary.com/castlery/image/private/w_1000,f_auto,q_auto/b_rgb:F3F3F3,c_fit/v1624964497/crusader/variants/40550131/Seb-Desk-Lifestyle-Crop.jpg" alt="">

        <img v-else-if="listingInfo['itemCategory'] == 'Electronics'" src="https://www.tds-office.com/wp-content/uploads/2018/10/office-electronics-printers-copiers.jpg" alt="">
        
        <img v-else-if="listingInfo['itemCategory'] == 'Office Supplies'" src="https://storables.com/wp-content/uploads/2020/06/AdobeStock_221435829-1024x684.jpeg" alt="">

        <img v-else src="../assets/—Pngtree—isometric and colorful warehouse_5511333.png"/>


        <div class="p-2">
            <div class="d-flex justify-content-between align-items-center">
                <p style="font-size:20px" class="desc">{{itemName}}</p>
                <small class="desc"><i class="fa-solid fa-smog"></i> {{emission}}</small>
            </div>
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
            itemName: "",
            company: "",
            department: "",
            emission: "",
            img: "",
            listingId: "",
            buyerId: ""
        }
    },
    mounted(){

        if (!this.offer && this.listingInfo){
            this.listingId = this.listingInfo._id
            this.company = this.listingInfo.company.companyName 
            this.department = this.listingInfo.department.departmentName 
            this.itemName = this.listingInfo.itemName
            this.emission =  this.listingInfo.carbonEmission

            this.listing = {}

        }
        if (this.offer && this.listingInfo) {

            this.listingId = this.listingInfo.itemId
            this.company = this.listingInfo.companyName 
            this.department = this.listingInfo.departmentName 
            this.itemName = this.listingInfo.itemName
            this.emission =  this.listingInfo.carbonEmission
            this.buyerId = this.listingInfo.buyerDepartmentId

        }
    },
    props: ["listingInfo", "offer"],
    methods: {

        // OFFER FUNCTIONS
        acceptOffer(){
            console.log("accept offer")

            var url = "http://localhost:3101/accept_item"

            axios.get(url, {
                params: {
                    itemId: this.listingId,
                    departmentId: this.buyerId
                }
            })
            .then(response => {
                console.log("item accept")
                console.log(response.data)
            })
            .catch(error => {
                console.log(error.message)
            })
            location.reload()
        },

        // LISTING FUNCTIONS
        viewMore(){
            console.log("view more")

            // set session variable to view listing
            sessionStorage.setItem("viewListing", JSON.stringify(this.listingInfo));

            // re-route to listing page
            this.$router.push({path: '/listing'});
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