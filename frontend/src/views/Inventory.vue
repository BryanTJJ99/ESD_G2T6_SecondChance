<template>
    <div>
        <TopNavbar :organization="organization" :department="department" />
        <Sidebar />
        <div class="container-flex d-flex justify-content-center p-3" style="margin-left: 4.5rem;">

            <div class="w-100 px-3 py-2">

                <div class="d-flex px-3 py-2 justify-content-between align-items-end">
                  
                    <h3>Inventory Management</h3>
                    <button class="btn btn-dark" data-bs-toggle="modal"
                        data-bs-target="#exampleModal"><span>Add Item</span></button>
   
                </div>



                <div class="input-group px-3 py-3">
                    <span class="input-group-text" style="background-color:#c5dad2;" id="inputGroup-sizing-default">
                        <p>Search</p>
                    </span>
                    <input type="text" class="form-control pt-3" aria-label="Sizing example input"
                        aria-describedby="inputGroup-sizing-default">
                </div>

                <div class="list-group px-3">
                    <button v-for="item in items" :key="item.id" type="button"
                        class="list-group-item list-group-item-action d-flex justify-content-between p-3 pt-3 ps-3">

                        <p>{{ item['name'] }} &nbsp; </p>

                        <div class="align-items-center">
                            <small>{{ item['category'] }}</small>

                            <!-- <span class="badge mx-3" style="background-color:#c5dad2; color: black; width: 100px;">
                                <p>Quantity : {{ item['Quantity'] }}</p>
                            </span> -->
                            <small class="mx-3">Quantity : {{ item['Quantity'] }}</small>

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

    </div>
</template>

<script>
import TopNavbar from "@/components/Navbar/TopNavbar.vue";
import Sidebar from "@/components/Navbar/Sidebar.vue";
import Container from "@/components/Container.vue";

export default {
    data() {
        return {
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
        Sidebar
    },
    methods: {
        addItem: function () {
            this.items.push({
                "name": this.newItem,
                "Quantity": this.newItemQty
            })

            this.newItem = "";
            this.newItemQty = 0;
        }
    }

}

</script>