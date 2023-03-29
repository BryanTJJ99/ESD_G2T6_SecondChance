import axios from "axios";


const API_URL = "http://localhost:8080/department";

class departmentService{

    getDepartmentById(departmentId) {
        const response = axios
          .get(API_URL + "/" + departmentId)
          .then((response) => {

            console.log("get request successful!");
            return response.data;

          })
          .catch((error) => {
            console.log("get request unsuccessful", error);
            return error;
          });
        return response;
    }

    getAllDepartments(){
        const response=axios
            .get(API_URL + "/allDepartments")
            .then((response)=>{

                console.log("Get Request Successful");
                return response.data;

            })
            .catch((error)=>{
                console.log("Get request unsuccessful", error)
                return error;
            })

            return response
    }

}
export default new departmentService()