<script>

</script>

<template>
  <div class="col-xl-3 col-md-6 pt-5 d-flex justify-content-center">
    <div class="card p-1">
        <img src="https://i.postimg.cc/1X8R7m8y/design.png"/>
        <div class="p-2">
            <div class="d-flex justify-content-between align-items-bottom">
                <p style="font-size:20px" class="desc">{{itemName}}</p>
                <small class="desc">{{status}}</small>
            </div>
            <i class="fa-solid fa-location-dot" style="color:#a3a0a0"><span class="desc ps-1">{{address}}</span></i>
            <i class="fa-solid fa-building d-block" style="color:#a3a0a0"><span class="desc ps-1">{{company}}, {{department}}</span></i>
        </div>

        <div class="card__content">
          <div class="d-flex justify-content-center mt-2">
            <button class="btn btn-light desc"><span>View More</span></button>
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
            status: "Like New",
            img: ""
        }
    },
    props: ["listingId"]
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