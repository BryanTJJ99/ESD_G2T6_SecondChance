<template>
    <div>
        <TopNavbar :organization="organization" :department="department" />
        <Sidebar />
        <div class="container-flex d-flex justify-content-center p-3" style="margin-left: 4.5rem;">

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
<<<<<<< Updated upstream
=======
                        <div class="input-group mb-3" style="position:relative">
                            <label for="newItemImage" class="input-group-text" style="background-color: #c5dad2; z-index: 2; width: 25%; height: 100%; position: absolute; top: 0; left: 0;">Choose file</label>
                            <input id="newItemImage" class="form-control"  @change="selectFile" style="z-index:1" type="file" multiple>
                        </div>
                        <div v-if="newItemImage.length">
                            <p>Uploaded Images:</p>
                            <div v-for="(img, index) in newItemImage" :key="index">
                              <img :src="img" alt="image" style="width: 200px; height: 200px;">
                            </div>
                        </div>
>>>>>>> Stashed changes
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
import AOS from 'aos'
import 'aos/dist/aos.css';

export default {
    mounted() {
        AOS.init({
            duration: 1300,
        })
    },
    data() {
        return {
            department: "Finance",
            organization: "SMU",
            newItem: "",
            newItemQty: 0,
<<<<<<< Updated upstream
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
=======
            channelId: "",
            channelKey: "",
            newItemImage:[],
            items: [],
>>>>>>> Stashed changes
        }
    },
    components: {
        TopNavbar,
        Sidebar
    },
    methods: {
        addItem: function () {
<<<<<<< Updated upstream
            this.items.push({
                "name": this.newItem,
                "Quantity": this.newItemQty
            })

            this.newItem = "";
            this.newItemQty = 0;
=======
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
                this.newItemImage.push(e.target.result)
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
>>>>>>> Stashed changes
        }
    }

}

</script>