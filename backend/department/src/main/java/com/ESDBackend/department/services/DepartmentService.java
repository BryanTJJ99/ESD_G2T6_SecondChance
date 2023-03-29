package com.ESDBackend.department.services;

import com.ESDBackend.department.models.Department;
import java.util.*;

public interface DepartmentService {

    public Department getDepartmentById(String departmentID);

    public List<Department> getAllDepartments();

    public Department addDepartmentItemId(String departmentID, String itemID);

    public Department deleteDepartmentItemId(String departmentID, String itemID);

    public double getDepartmentCarbonSaved(String departmentID);

    public void addDepartmentCarbonSaved(String departmentID, double carbonAmt);

}
