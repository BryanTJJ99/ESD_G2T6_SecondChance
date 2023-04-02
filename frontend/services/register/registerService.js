import axios from "axios";
const DEPT_URL = 'http://localhost:8080/department'
const COMPANY_URL = 'http://localhost:5001'

class registerService{

    // ADD NEW DEPARTMENT
    addDepartment(dept){

        const response = axios
        .post(DEPT_URL + '/create', dept)
            .then(response => {
    
                // console.log(response.data)
                console.log("dept added successfully")

                return response
    
            })
            .catch(error => {
                console.log(error.message)
    
            })
        return response
    }

    addCompany(company){
        const response = axios
        .post(COMPANY_URL + "/create", company)
            .then(response => {
                // console.log(response.data)
                console.log("company added successfully")

                return response
            })
            .catch(error => {
                console.log(error.message)
            })
        return response
    }

    updateDepartment(dept, deptId){
        const response = axios
        .put(DEPT_URL + "/update/" + deptId, dept
    )
        .then(response => {

            console.log(response.data)
            console.log("dept modified successfully")
        })
        .catch(error => {
            console.log(error.message)

        })
        return response

    }

    updateCompany(company, companyId){
        const response = axios
        .put(COMPANY_URL + "/edit/" + companyId, company)
        .then(response => {

            console.log(response.data)
            console.log("company modified successfully")
        })
        .catch(error => {
            console.log(error.message)

        })
        
        return response
    }

}
export default new registerService;