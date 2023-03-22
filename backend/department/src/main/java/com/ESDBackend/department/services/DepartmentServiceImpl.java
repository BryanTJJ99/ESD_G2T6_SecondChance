package com.ESDBackend.department.services;
import com.ESDBackend.department.models.Department;
import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PutMapping;





@RestController
@RequestMapping("/department")
public class DepartmentServiceImpl {

    @Autowired
    private DepartmentDAO DepartmentDAO;

    @PutMapping("/departments/{departmentID}")
    public int addItem(@PathVariable String departmentID, @RequestBody String itemID) {
        return DepartmentDAO.addItem(departmentID, itemID);
    }

    @GetMapping("/department/{departmentID}")
    public ArrayList<String> getDepartmentItems(@PathVariable String departmentID) {
        return DepartmentDAO.getDepartmentItems(departmentID);
    }

    @PutMapping("/department/{departmentID}")
    public int removeItem(@PathVariable String departmentID, @RequestBody String itemID) {
        return DepartmentDAO.removeItem(departmentID, itemID);
    }
}




    // public int addItem(String itemID){
    //     try {

    //         dept.addItem(itemID);
    //         return 200;

    //     } catch (Exception e) {

    //         System.out.println(e.getMessage());
    //         return 400;

    //     }
        
    // }

    // public List<String> getDepartmentItems(){
    //     try {

    //         return dept.getItems();

    //     } catch (Exception e) {

    //         System.out.println(e.getMessage());
    //         return null;

    //     }
    // }

    // public int removeItem(String itemID){
    //     try {
    //         dept.removeItem(itemID);
    //         return 200;
    //     } catch (Exception e) {
    //         System.out.println(e.getMessage());
    //         return 400;
    //     }

    // }

    // public int itemTransfer(Department receivingDepartment, String itemID){
    //     try {
    //         receivingDepartment.addItem(itemID);
    //         dept.removeItem(itemID);
    //         return 200;
    //     } catch (Exception e) {
    //         System.out.println(e.getMessage());
    //         return 400;
    //     }

    // }