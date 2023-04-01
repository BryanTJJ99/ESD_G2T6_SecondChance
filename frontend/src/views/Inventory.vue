<template>
    <div>
        <TopNavbar :organization="organization" :department="department" />
        <Sidebar />
        <div class="container-flex d-flex justify-content-center p-3" style="margin-left: 4.5rem;height:100vh;">

            <div class="w-100 px-3 py-2">

                <div class="d-flex px-3 py-2 justify-content-between align-items-end" data-aos="fade-down">
                  
                    <h3 data-aos="fade-down">Inventory Management</h3>

                    <div class="d-flex justify-content-end">

                        <button class="btn btn-dark" data-bs-toggle="modal"
                            data-bs-target="#exampleModal" data-aos="fade-down"><span>Add Item</span></button>
                        <button class="btn btn-dark" data-bs-toggle="modal"
                        data-bs-target="#channelModal" data-aos="fade-down"><span>Enable Notifications</span></button>

                    </div>
   
                </div>



                <!-- <div class="input-group px-3 py-3">
                    <span class="input-group-text" style="background-color:#c5dad2;" id="inputGroup-sizing-default" data-aos="fade-up">
                        <p>Search</p>
                    </span>
                    <input type="text" class="form-control pt-3" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-default" data-aos="fade-up">
                </div> -->

                <div class="list-group px-3" data-aos="fade-up">
                    <button v-for="item in depItems" type="button" :key="item.id"
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
                            <input type="text" v-model="newItem" class="form-control" placeholder="Item Name"
                                aria-label="itemName" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemQty">
                                <p>Quantity</p>
                            </span>
                            <input type="number" v-model="newItemQty" class="form-control" placeholder="Qty. No"
                                aria-label="newItemQty" aria-describedby="basic-addon1">
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
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="addItem">Save changes</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal fade" id="marketModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5 title" id="exampleModalLabel">Sell Item</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemForm">
                                <p>Item Name</p>
                            </span>
                            <input type="text" v-model="newItem" class="form-control" placeholder="Item Name"
                                aria-label="itemName" aria-describedby="basic-addon1">
                        </div>
                        <div class="input-group mb-3">
                            <span class="input-group-text" style="background-color:#c5dad2;" id="newItemQty">
                                <p>Quantity</p>
                            </span>
                            <input type="number" v-model="newItemQty" class="form-control" placeholder="Qty. No"
                                aria-label="newItemQty" aria-describedby="basic-addon1">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                        <button class="btn btn-dark" type="button" @click="addItem">Post On Marketplace</button>
                    </div>
                </div>
            </div>
        </div>

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


        departmentService.getDepartmentById("641d7448835767ff182d7c43")
        .then(response =>{
            console.log("Response Successful")
            this.depDetails = response;
            console.log(this.depDetails)

            for(let i = 0; i < response.itemIdArrayList.length; i++){

                console.log("getting " + response.itemIdArrayList[i])
                itemService.getItem(response.itemIdArrayList[i])
                .then(response => {
                    this.depItems.push(response.data);
                    console.log(this.depItems)

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
            deptId:'',
            depDetails : undefined,
            depItems : [],
            department: "Finance",
            organization: "SMU",
            newItem: "",
            newItemQty: 0,
            channelId: "",
            channelKey: "",
            images:[],
        }
    },
    components: {
        TopNavbar,
        Sidebar,
        Footer
    },
    methods: {
        addItem: function () {
            this.items.push({
                "name": this.newItem,
                "Quantity": this.newItemQty
            })
            console.log(this.depItems)

            this.newItem = "";
            this.newItemQty = 0;
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
        },
        addChannel(){

            // direct call to slack MS

            var url = ''

            axios.post(url, {
                deptId: this.deptId,
                channelId: this.channelId,
                channelKey: this.channelKey
            })
            .then(response => {
                console.log("yay")
            })
            .catch(error => {
                console.log(error.message)
                
            })
        }
    }
}

</script>