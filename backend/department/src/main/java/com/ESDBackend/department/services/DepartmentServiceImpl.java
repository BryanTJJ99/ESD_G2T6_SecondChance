package com.ESDBackend.department.services;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

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

    @Override
    public double getDepartmentCarbon(String departmentID) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            return department.getTotalCarbonSaved();
        }
        return -1;
    }


    @Override
    public void addDepartmentCarbonSaved(String departmentID, double carbonAmt) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            department.setTotalCarbonSaved(carbonAmt + department.getTotalCarbonSaved());
            departmentRepository.save(department);
            System.out.println("Added carbon saved of " + carbonAmt + "kgco2e to department " + departmentID);
        } else {
            System.out.println("Error: unable to add carbon saved of " + carbonAmt + "kgco2e to department " + departmentID);
        }
        
    }

}
