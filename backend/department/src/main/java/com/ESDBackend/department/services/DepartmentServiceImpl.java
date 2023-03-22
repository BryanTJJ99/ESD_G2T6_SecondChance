package com.ESDBackend.department.services;
import com.ESDBackend.department.models.Department;
import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;




@RestController
@RequestMapping("/department")
public class DepartmentServiceImpl implements DepartmentService {

    @Autowired
    private DepartmentService departmentService;

    @PostMapping("/items")
    public int addItem(@RequestParam("itemID") String itemID) {
        return departmentService.addItem(itemID);
    }

    @GetMapping("/items")
    public List<String> getDepartmentItems() {
        return departmentService.getDepartmentItems();
    }

    @DeleteMapping("/items/{itemID}")
    public int removeItem(@PathVariable("itemID") String itemID) {
        return departmentService.removeItem(itemID);
    }

    @PutMapping("/items/{itemID}")
    public int itemTransfer(@RequestBody Department receivingDepartment, 
                            @PathVariable("itemID") String itemID) {
        return departmentService.itemTransfer(receivingDepartment, itemID);
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