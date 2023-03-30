import axios from "axios";
const API_URL = "http://localhost:5001/"

class companyService{

    getCompanyById(companyId){
        const response = axios.get(API_URL + companyId)
        .then((response) => {
            console.log("get Company successful")
            return response;
        })
        .catch((error) =>{
            console.log("get company unsuccessful")
            return error
        })
        return response;
    }

}
export default new companyService;