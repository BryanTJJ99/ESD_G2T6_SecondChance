import axios from "axios";

const API_URL = "http://localhost:5002/search"

class carbonRetrieverService{
    getCarbonAmt(name, category){
        const response = axios.get(API_URL, {
            params:{
                name : name,
                category: category
            }
        })
        .then((response) => {
            console.log("Get Carbon Successful")
            return response
        })
        .catch((error) => {
            console.log("Get Carbon unsuccessful")
            return error
        })
    return response;

    }
}
export default new carbonRetrieverService