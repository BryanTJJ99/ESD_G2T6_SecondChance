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

                <div class="list-group px-3 mt-3" data-aos="fade-up">
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
            companyId: '',
            deptName: '',
            companyId: '',
            noItems: false,
            depDetails : undefined,
            depItems : [],
            department: "Finance",
            organization: "SMU",
            newItem: "",
            newItemQty: 0,
            items: [
                {
                    "name": "Ikea Dalgon",
                    "category": "Furniture",
                    "Quantity": 4
                },
                {
                    "name": "Swiss Candace",
                    "category": "Furniture",
                    "Quantity": 10
                },
                {
                    "name": "Woo Jablomi",
                    "category": "Equipment",
                    "Quantity": 5
                },
                {
                    "name": "Big ForceKin",
                    "category": "Electronics",
                    "Quantity": 10
                },
                {
                    "name": "Vicky",
                    "category": "Office Supplies",
                    "Quantity": 1
                },
            ],
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
        addItem: function () {
        this.items.push({
            "name": this.newItem,
            "Quantity": this.newItemQty,
            "image": this.newItemImage
        })

        console.log(this.items)

        this.newItem = "";
        this.newItemQty = 0;
        this.newItemImage = []
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