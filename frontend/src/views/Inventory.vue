<template>
    <div>
        <TopNavbar/>
        <Sidebar />
        <div class="container-flex d-flex justify-content-center p-3" style="margin-left: 4.5rem;height:100vh;">

            <div class="w-100 px-3 py-2">

                <div class="d-flex px-3 py-2 justify-content-between align-items-end" data-aos="fade-down">
                  
                    <h3 data-aos="fade-down">Inventory Management</h3>

                    <div class="d-flex justify-content-end">

                        <button class="btn btn-dark" data-bs-toggle="modal"
                            data-bs-target="#exampleModal" data-aos="fade-down"><span>Add Item</span></button>
                        
                    </div>
   
                </div>

                <div v-if="noItems" data-aos="fade-down">
                    <small class="text-center px-3">There are no items in your inventory.</small>
                </div>


                <!-- <div class="input-group px-3 py-3">
                    <span class="input-group-text" style="background-color:#c5dad2;" id="inputGroup-sizing-default" data-aos="fade-up">
                        <p>Search</p>
                    </span>
                    <input type="text" class="form-control pt-3" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-default" data-aos="fade-up">
                </div> -->

                <div class="list-group px-3 mt-3" data-aos="fade-up">
                    <template v-for="item in depItems">
                        <!--LISTED-->
                        <button v-if="item.isListed" type="button" :value="item.id"
                            class="list-group-item list-group-item-action d-flex justify-content-between p-3 pt-3 ps-3">

                            <p>{{ item.itemName }} &nbsp; </p>

                            <div class="align-items-center">
                                <small class="mx-3">{{ item.itemCategory.toUpperCase() }}</small>

                                <!-- <span class="badge mx-3" style="background-color:#c5dad2; color: black; width: 100px;">
                                    <p>Quantity : {{ item['Quantity'] }}</p>
                                </span> -->
                                <!-- <i class="fa-regular fa-store mr-3" data-bs-toggle="modal"
                                data-bs-target="#marketModal" style="color: grey;"></i> -->
                                <i class="fa-solid fa-store-slash mr-3" data-bs-toggle="modal"
                                data-bs-target="#removeMarketModal" style="color: grey;" ></i>
                                
                            </div>
                            
                        </button>
                        <!--NOT LISTED-->
                        <button  v-else type="button" :value="item.id"
                            class="list-group-item list-group-item-action d-flex justify-content-between p-3 pt-3 ps-3">

                            <p>{{ item.itemName }} &nbsp; </p>

                            <div class="align-items-center">
                                <small class="mx-3">{{ item.itemCategory.toUpperCase() }}</small>

                                <!-- <span class="badge mx-3" style="background-color:#c5dad2; color: black; width: 100px;">
                                    <p>Quantity : {{ item['Quantity'] }}</p>
                                </span> -->
                                <i class="fa-regular fa-store mr-3" data-bs-toggle="modal"
                                data-bs-target="#marketModal" style="color: grey;"></i>
                            </div>
                            
                        </button>
                    </template>


                </div>
            </div>
        </div>
      

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5 title" id="exampleModalLabel">Add Item</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemForm">
                                <p>Item Name</p>
                            </span>
                            <input type="text" v-model="newItemName" class="form-control" placeholder="Item Name"
                                aria-label="itemName" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemForm">
                                <p>Item Category</p>
                            </span>
                            <input type="text" v-model="newItemCategory" class="form-control" placeholder="Item Name"
                                aria-label="itemCategory" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3" style="position:relative">
                            <label for="image" class="input-group-text" style="background-color: #c5dad2; z-index: 2; width: 25%; height: 100%; position: absolute; top: 0; left: 0;">Choose file</label>
                            <input id="image" class="form-control"  @change="selectFile" style="z-index:1" type="file" multiple>
                        </div>
                        <div v-if="images.length">
                            <p>Uploaded Images:</p>
                            <div v-for="(img, index) in images" :key="index">
                              <img :src="img" alt="image" style="width: 200px; height: 200px;">
                            </div>
                        </div>
                        <!-- <div class="input-group mb-3" style="position:relative">
                            <label for="image" class="input-group-text" style="background-color: #c5dad2; z-index: 2; width: 25%; height: 100%; position: absolute; top: 0; left: 0;">Choose file</label>
                            <input id="image" class="form-control"  @change="selectFile" style="z-index:1" type="file" multiple>
                        </div> -->
                        <!-- <div v-if="images.length">
                            <p>Uploaded Images:</p>
                            <div v-for="(img, index) in images" :key="index">
                              <img :src="img" alt="image" style="width: 200px; height: 200px;">
                            </div>
                        </div> -->
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="addItem" data-bs-dismiss="modal">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
        <!--MARKET MODAL-->
        <div class="modal fade" id="marketModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5 title" id="exampleModalLabel">Sell Item</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <select name="" class="form-control" v-model="itemToChange">
                            <option v-for="item in unlistedItems" :value="item">{{ item.itemName }}</option>
                        </select>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="changeMarketPlace(true)">Post On Marketplace</button>
                    </div>
                </div>
            </div>
        </div>

        <!--CHANNEL MODAL-->
        <div class="modal fade" id="channelModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5 title" id="exampleModalLabel">Enable Slack Notifications</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>

                    <div class="modal-body">
                        <small>Receive notifications to your Slack channel on your listings and offers.</small>

                        <div class="input-group my-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemForm">
                                <p>Channel ID:</p>
                            </span>
                            <input type="text" v-model="channelId" class="form-control" 
                                aria-label="itemName" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemQty">
                                <p>Key:</p>
                            </span>
                            <input type="text" v-model="channelKey" class="form-control" 
                                aria-label="newItemQty" aria-describedby="basic-addon1">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="addChannel">Enable</button>
                    </div>
                </div>
            </div>
        </div>

        <!--REMOVE FROM MARKET-->
        <div class="modal fade" id="removeMarketModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5 title" id="exampleModalLabel">Remove Item from Market</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <select name="" class="form-control" v-model="itemToChange">
                            <option v-for="item in listedItems" :value="item">{{ item.itemName }}</option>
                        </select>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="changeMarketPlace(false)">Remove From Marketplace</button>
                    </div>
                </div>
            </div>
        </div>

        <Footer style="margin-left:4.5rem;"></Footer>
    </div>
</template>

<script>
import TopNavbar from "@/components/Navbar/TopNavbar.vue";
import Sidebar from "@/components/Navbar/Sidebar.vue";
import Container from "@/components/Container.vue";
import Footer from "@/components/Footer.vue";
import AOS from 'aos';
import 'aos/dist/aos.css';
import departmentService from "../../services/department/departmentService";
import itemService from "../../services/items/itemService";
import carbonRetrieverService from "../../services/carbonretriever/carbonRetrieverService"
import axios from "axios";

import { getAuth, onAuthStateChanged} from "firebase/auth";

export default {
   
    mounted() {
        AOS.init({
            duration: 1300,
        })

        this.checkuser()
        this.deptId = sessionStorage.getItem("deptId")
        this.companyId = sessionStorage.getItem("companyId")
        this.deptName = sessionStorage.getItem("deptName")
        this.companyName = sessionStorage.getItem("companyName")

        departmentService.getDepartmentById(this.deptId)
        .then(response =>{
            console.log("Response Successful")
            this.depDetails = response;
            console.log(this.depDetails)

            if (response.itemIdArrayList.length == 0){
                this.noItems = true
            }

            for(let i = 0; i < response.itemIdArrayList.length; i++){
                this.noItems = false
                console.log("getting " + response.itemIdArrayList[i])
                itemService.getItem(response.itemIdArrayList[i])
                .then(response => {
                    if(response.data['isListed']){
                        this.listedItems.push(response.data)
                    }
                    else{
                        this.unlistedItems.push(response.data)
                    }
                    this.depItems.push(response.data);
                    console.log(this.listedItems)
                    console.log(this.unlistedItems)

                    // carbonRetrieverService.getCarbonAmt(response.data.itemName, response.data.itemCategory)
                    // .then(response =>{
                    //     console.log(response)

                    // })
                })
            }
        });
      
    },
    data() {
        return {
            unlistedItems : [],
            itemToChange:"",
            listedItems:[],
            deptId:"",
            companyId: '',
            deptName: '',
            companyId: '',
            noItems: false,
            depDetails : undefined,
            depItems : [],
            department: "Finance",
            organization: "SMU",
            newItemName: "",
            newItemCategory : "",
            newItemId: undefined,

            channelId: "",
            channelKey: "",
            newItemImage:[],
            items: [],
            images: []
        }
    },
    components: {
        TopNavbar,
        Sidebar,
        Footer
    },

    methods: {
        addItem: async function () {
            try{
                var data = {
                "itemName" : this.newItemName,
                "itemCategory" : this.newItemCategory,
                "isListed": false,
                "itemPicture": "Random Picture",
                "itemDescription": "Random Description",
                "carbonEmission": 0,
                "buyerIds": [],
                "companyId": this.companyId,
                "departmentId": this.deptId
                }

                var carbon_response = await carbonRetrieverService.getCarbonAmt("chair", "furniture")
                var carbon_amt = carbon_response.data
                data['carbonEmission'] = carbon_amt;
                console.log(carbon_amt)

                console.log(data)
                var item_response = await itemService.createItem(data)
                console.log(item_response)
                var itemId = item_response.data.data.item._id.$oid;
                console.log(itemId)

                departmentService.addItemToDept(this.deptId, itemId )
                .then((response) =>{
                    console.log("ITEM Added to dept" + response)
                })
                .catch((error)=>{
                    console.log("Item not added to dept " + error)
                })

                this.depItems.push({
                    "itemName": this.newItemName,
                    "itemCategory": this.newItemCategory
                })
                console.log(this.depItems)
                this.newItemName = "";
                this.newItemCategory = "";
                location.reload()
            }
            catch(error){
                console.log(error)
                return error
            }

           
        },

        changeMarketPlace(changeTo){
            // console.log(this.itemToRemoveFromMarket)
            // this.itemToRemoveFromMarket['isListed'] = false;
            var data = {   "buyerIds" : this.itemToChange['buyerIds'],
                            "carbonEmission" : this.itemToChange['carbonEmission'],
                            "companyId" : this.itemToChange['companyId'],
                            "departmentId" : this.itemToChange['departmentId'],
                            "isListed" : changeTo,
                            "itemCategory" : this.itemToChange['itemCategory'],
                            "itemDescription":this.itemToChange['itemDescription'],
                            "itemName" : this.itemToChange['itemName'],
                            "itemPicture" : this.itemToChange['itemPicture']
                        }


            itemService.editItem(data, this.itemToChange['_id'].$oid)
            .then((response) =>{
                console.log("ITEM SUCCESSFULLY REMOVED FROM MARKET")
            })
            .catch((error)=>{
                console.log("Item NOT removed from market")
            })
            location.reload()
        },

        selectFile(e) {
            const files = e.target.files
            for (let i = 0; i < files.length; i++) {
                const image = files[i]
                const reader = new FileReader()
                reader.readAsDataURL(image)
                reader.onload = e => {
                this.images.push(e.target.result)
                }
            }
        },

        checkuser(){
            const auth = getAuth();
            onAuthStateChanged(auth, (user) => {
                if (!user) {
                    console.log('user is not logged in')
                    window.location.href = `/`;
                }
            });
        }   
    }
}

</script>