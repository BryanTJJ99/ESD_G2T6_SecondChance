<template>
    <div>
        <TopNavbar :organization="organization" :department="department" />
        <Sidebar />
        <div class="container-flex d-flex justify-content-center p-3" style="margin-left: 4.5rem;height:100vh;">

            <div class="w-100 px-3 py-2">

                <div class="d-flex px-3 py-2 justify-content-between align-items-end" data-aos="fade-down">
                  
                    <h3 data-aos="fade-down">Inventory Management</h3>
                    <button class="btn btn-dark" data-bs-toggle="modal"
                        data-bs-target="#exampleModal" data-aos="fade-down"><span>Add Item</span></button>
   
                </div>



                <div class="input-group px-3 py-3">
                    <span class="input-group-text" style="background-color:#c5dad2;" id="inputGroup-sizing-default" data-aos="fade-up">
                        <p>Search</p>
                    </span>
                    <input type="text" class="form-control pt-3" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-default" data-aos="fade-up">
                </div>

                <div class="list-group px-3" data-aos="fade-up">
                    <button v-for="item in depItems" type="button"
                        class="list-group-item list-group-item-action d-flex justify-content-between p-3 pt-3 ps-3">

                        <p>{{ item }} &nbsp; </p>

                        <div class="align-items-center">
                            <small class="mx-3">{{ item['category'] }}</small>

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
import axios from "axios";


export default {
   
    mounted() {
        AOS.init({
            duration: 1300,
        })

        departmentService.getDepartmentById("641d7448835767ff182d7c43")
        .then(response =>{
            console.log("Response Successful")
            this.depDetails = response;
            this.depItems = response.itemIdArrayList
            console.log(this.depDetails)
            console.log(this.depItems)
        });
      
    },
    data() {
        return {
            depDetails : undefined,
            depItems : undefined,
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
            ]
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

        // getInventory(){
        //     var departmentUrl = ""
        //     var itemUrl = ""
        //     var depItems = []
            
        //     // call department service to retrieve departmentItems
        //     axios.get(departmentUrl,{
        //         params:{
        //             departmentID :this.department,
        //         }
        //     })
        //     .then(response => {
        //         if(len(response.itemIdArrayList) > 0){
        //             depItems = response.itemIdArrayList
        //         }
        //     })
        //     .catch(error=>{
        //         console.log(error.message)
        //         return
        //     })

        //     //get each item by invoking item microservice
        //     for (let i = 0; i < depItems.len; i++){
        //        axios.get(itemUrl,{
        //         params: {
        //             itemId : depItems[i]
        //         }
        //        })
        //        .then(response => {})
        //        .catch(error => {})
        //     }   
        // },
        

        // addItem(){
        //     departmentUrl = ""
        //     itemUrl = ""
        //     axios.get()
        // }
    }
}

</script>