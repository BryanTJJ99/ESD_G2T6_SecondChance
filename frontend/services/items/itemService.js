import axios from "axios";


const API_URL = "http://localhost:5000/";

class itemService{

    getItem(itemId){
        const response = axios.get(API_URL + itemId)
        .then((response) =>{
            console.log("Get Item Successful");
            return response;
        })
        .catch((error)=>{
            console.log("Get Item Unsuccessful" + error);
            return error;
        })
        return response;
    }

    getAllItems(){
        const response = axios.get(API_URL + "all")
        .then((response) => {
            console.log("Get all items successfull");
            return response;
        })
        .catch((error) => {
            console.log("Get all items unsuccessful" + error)
            return error;
            
        })

        return response;
    }
    
    createItem(data){
        const response = axios.post(API_URL + "create", data)
        .then((response)=>{
            console.log("Item create called successfully")
            return response;
        })
        .catch((error)=>{
            console.log("Item create called UNsuccessfully");
            return error
        })
        return response
    }

    editItem(data, itemId){
        const response = axios.put(API_URL + "edit/" + itemId, data)
        .then((response) => {
            console.log("Item edited successfully")
            return response
        })
        .catch((error)=>{
            console.log("Item edited unsuccessfully" + error)
            return error
        })
        return response
    }

}
export default new itemService()