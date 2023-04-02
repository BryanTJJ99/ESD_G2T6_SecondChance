import axios from "axios";


const API_URL = "http://localhost:3004/";

class itemDetailsService{

    getDepartmentOffers(departmentID){
        const response = axios.get(API_URL + "department" + "/" + departmentID)
        .then((response)=>{
            console.log("Get Department Offers Successful")
            return response
        })
        .catch((error)=>{
            console.log("Get department offers NOT successful " + error)
            return error
        })

        return response
    }

}
export default new itemDetailsService()