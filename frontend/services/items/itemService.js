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

}
export default new itemService()