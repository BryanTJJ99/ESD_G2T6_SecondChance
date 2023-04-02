package com.ESDBackend.department.services;

import com.ESDBackend.department.models.Department;
import java.util.*;

public interface DepartmentService {

    public Department getDepartmentById(String departmentID);

    public List<Department> getAllDepartments();

    public Department addDepartmentItemId(String departmentID, String itemID);

    public Department deleteDepartmentItemId(String departmentID, String itemID);

    public double getDepartmentCarbon(String departmentID);

    public void addDepartmentCarbon(String departmentID, double carbonAmt);

    public Department getDepartmentByEmail(String email);

    public String getCompanyIdByDepartmentNameAndPostalCode(String departmentName, String postalCode);

    public Department addDepartment(Department department);

    public Department updateDepartment(String departmentId, Department department);

}
