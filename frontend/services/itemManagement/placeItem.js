import axios from "axios";


const API_URL = "http://localhost:3006/place_item";

class PlaceItem{

    placeItem(data){
        const response = axios.post(API_URL, data)
        .then((response) => {
            console.log("Place Item Successful")
            return response
        })
        .get((error) => {
            console.log("Place Item Not Successful")
            return error
        })
        return response
    }

}
export default new PlaceItem()