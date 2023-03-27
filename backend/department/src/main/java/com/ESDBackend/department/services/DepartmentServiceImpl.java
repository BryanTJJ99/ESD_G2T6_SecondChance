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
    public ArrayList<String> getDepartmentItemsIDList(String departmentID) {
        Optional<Department> optionalDepartment = departmentRepository.findById(departmentID);
        if (optionalDepartment.isPresent()) {
            System.out.println("have");
            return (ArrayList<String>) optionalDepartment.get().getItemIdArrayList();
        } else {
            System.out.println("dont have");
            return null;
        }
    }


    @Override
    public Department addDepartmentItemId(String departmentID, String itemID) {
        Department department = departmentRepository.findById(departmentID).get();
        if (department != null) {
            System.out.println("have");
            department.addItem(itemID);
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
            System.out.println("have");
            department.removeItem(itemID);
            return departmentRepository.save(department);
        }
        return null;
    }



}





