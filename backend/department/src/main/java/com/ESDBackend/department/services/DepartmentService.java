package com.ESDBackend.department.services;
import com.ESDBackend.department.models.Department;
import java.util.*;



public interface DepartmentService {
    public int addItem(String itemID);

    public List<String> getDepartmentItems();

    public int removeItem(String itemID);

    public int itemTransfer(Department receivingDepartment, String itemID);
    
}
