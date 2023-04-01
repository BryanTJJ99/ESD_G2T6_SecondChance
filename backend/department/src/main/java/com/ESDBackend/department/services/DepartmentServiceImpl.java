package com.ESDBackend.department.services;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.CrossOrigin;

import com.ESDBackend.department.models.Department;
import com.ESDBackend.department.repositories.DepartmentRepository;

@Service
public class DepartmentServiceImpl implements DepartmentService {

    @Autowired
    private DepartmentRepository departmentRepository;

    @Override
    public List<Department> getAllDepartments() {
        return departmentRepository.findAll();
    }

    @Override
    public Department getDepartmentById(String departmentID) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            System.out.println("Successful");
            return department;
        } else {
            System.out.println("Unsuccessful");
            return null;
        }
    }

    @Override
    public Department addDepartmentItemId(String departmentID, String itemID) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            List<String> itemIdArr = department.getItemIdArrayList();
            if (itemIdArr.contains(itemID)) {
                System.out.println("This item already exists inside the department");
            } else {
                department.addItem(itemID);
                System.out.println("Added successfully");
            }
            // List<String> itemArr = department.getItemIdArrayList();
            // itemArr.add(itemID);
            // department.setItemIdArrayList(itemArr);
            return departmentRepository.save(department);
        }
        return null;
    }

    @Override
    public Department deleteDepartmentItemId(String departmentID, String itemID) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            List<String> itemIdArr = department.getItemIdArrayList();
            if (itemIdArr.contains(itemID)) {
                department.removeItem(itemID);
                System.out.println("Removed successfully");
                return departmentRepository.save(department);
            } else {
                System.out.println("This item does not exist inside the department");
                return null;
            }
            
        }
        return null;
    }

    // @Override
    // public double getDepartmentCarbon(String departmentID) {
    //     Department department = departmentRepository.findById(departmentID).get();
    //     if (department != null) {
    //         return department.getTotalCarbon();
    //     }
    //     return -1;
    // }
    @Override
    public double getDepartmentCarbon(String departmentID) {
        Optional<Department> department = departmentRepository.findById(departmentID);
        if (department.isPresent()) {
            return department.get().getTotalCarbon();
        }
    // Alternatively, you could throw an exception here to indicate that the department was not found.
    // throw new IllegalArgumentException("Department not found for ID: " + departmentID);
    return -1;
    }



    @Override
    public void addDepartmentCarbon(String departmentID, double carbonAmt) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            department.setTotalCarbon(carbonAmt + department.getTotalCarbon());
            departmentRepository.save(department);
            System.out.println("Added carbon saved of " + carbonAmt + "kgco2e to department " + departmentID);
        } else {
            System.out.println("Error: unable to add carbon saved of " + carbonAmt + "kgco2e to department " + departmentID);
        }
        
    }


    @Override
    @CrossOrigin
    public Department getDepartmentByEmail(String email) {
        Department department = departmentRepository.findByEmail(email).get();
        if (department != null) {
            System.out.println("Retrieved departmentID by email successfully");
            return department;
        } else {
            System.out.println("Failed retrieval of departmentID by email");
            return null;
        }
    }


    @Override
    @CrossOrigin
    public String getCompanyIdByDepartmentNameAndPostalCode(String departmentName, String postalCode) {
        Optional<Department> department = departmentRepository.findByDepartmentNameAndPostalCode(departmentName, postalCode);
        if (department.isPresent()) {
            System.out.println("Retrieved departmentID by department name and postal code successfully");
            return department.get().getCompanyId();
        } else {
            System.out.println("Failed retrieval of departmentID by department name and postal code");
            return null;
        }
    }
    

}
