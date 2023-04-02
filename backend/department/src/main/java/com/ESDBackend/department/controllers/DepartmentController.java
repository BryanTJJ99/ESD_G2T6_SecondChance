package com.ESDBackend.department.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.ESDBackend.department.models.Department;
// import com.ESDBackend.department.repositories.DepartmentDAO;
import com.ESDBackend.department.services.DepartmentService;

@RestController
@RequestMapping("/department")
public class DepartmentController {

    @Autowired
    // @Qualifier("departments")
    private DepartmentService departmentService;

    @GetMapping("/allDepartments")
    @CrossOrigin
    public List<Department> getAllDepartments() {
        System.out.println("Testing");
        return departmentService.getAllDepartments();
    }

    @GetMapping("/{departmentID}")
    @CrossOrigin
    public Department getDepartmentById(@PathVariable String departmentID) {
        System.out.println("Testing1");
        return departmentService.getDepartmentById(departmentID);
    }

    @PostMapping("/addItemID/{departmentID}/{itemID}")
    @CrossOrigin
    public Department addDepartmentItemId(@PathVariable("departmentID") String departmentID,
            @PathVariable("itemID") String itemID) {
        return departmentService.addDepartmentItemId(departmentID, itemID);
    }

    @DeleteMapping("/deleteItemID/{departmentID}/{itemID}")
    @CrossOrigin
    public Department deleteDepartmentItemId(@PathVariable("departmentID") String departmentID,
            @PathVariable("itemID") String itemID) {
        return departmentService.deleteDepartmentItemId(departmentID, itemID);
    }

    @GetMapping("/getDepartmentCarbon/{departmentID}")
    @CrossOrigin
    public double getDepartmentCarbon(@PathVariable String departmentID) {
        return departmentService.getDepartmentCarbon(departmentID);
    }

    @PutMapping("/addDepartmentCarbon/{departmentID}/{carbonAmount}")
    @CrossOrigin
    public void addDepartmentCarbon(@PathVariable("departmentID") String departmentID,
            @PathVariable("carbonAmount") double carbonAmt) {
        departmentService.addDepartmentCarbon(departmentID, carbonAmt);
    }

    @GetMapping("/getDepartmentIdByEmail/{email}")
    @CrossOrigin
    public Department getDepartmentIdByEmail(@PathVariable String email) {
        return departmentService.getDepartmentByEmail(email);
    }

    @GetMapping("/getCompanyIdByDepartmentNameAndPostalCode/{departmentName}/{postalCode}")
    @CrossOrigin
    public String getCompanyIdByDepartmentNameAndPostalCode(@PathVariable("departmentName") String departmentName,
            @PathVariable("postalCode") String postalCode) {
        return departmentService.getCompanyIdByDepartmentNameAndPostalCode(departmentName, postalCode);
    }

    @PostMapping("/create")
    @CrossOrigin
    @ResponseStatus(HttpStatus.CREATED)
    public Department addDepartment(@RequestBody Department department) {
        return departmentService.addDepartment(department);
    }

    @PutMapping("/update/{departmentId}")
    @CrossOrigin
    public Department updateDepartment(@PathVariable String departmentId,@RequestBody Department newDepartment) {
        return departmentService.updateDepartment(departmentId,newDepartment);
    }

}
