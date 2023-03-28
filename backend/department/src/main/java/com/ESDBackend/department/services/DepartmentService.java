package com.ESDBackend.department.services;

import com.ESDBackend.department.models.Department;
import java.util.*;

public interface DepartmentService {

    public ArrayList<String> getDepartmentItemsIDList(String departmentID);

    public List<Department> getAllDepartments();

    public Department addDepartmentItemId(String departmentID, String itemID);

    public Department deleteDepartmentItemId(String departmentID, String itemID);

    public double getDepartmentCarbon(String departmentID);

    public void addDepartmentCarbon(String departmentID, double carbonToAdd);

}
