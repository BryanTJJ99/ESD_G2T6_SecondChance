package com.ESDBackend.department.services;
import com.ESDBackend.department.models.Department;
import java.util.*;



public class DepartmentServiceImpl implements DepartmentService {
    private Department dept;

    public int addItem(String itemID){
        try {

            dept.addItem(itemID);
            return 200;

        } catch (Exception e) {

            System.out.println(e.getMessage());
            return 400;

        }
        
    }

    public List<String> getDepartmentItems(){
        try {

            return dept.getItems();

        } catch (Exception e) {

            System.out.println(e.getMessage());
            return null;

        }
    }

    public int removeItem(String itemID){
        try {
            dept.removeItem(itemID);
            return 200;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return 400;
        }

    }

    public int itemTransfer(Department receivingDepartment, String itemID){
        try {
            receivingDepartment.addItem(itemID);
            dept.removeItem(itemID);
            return 200;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return 400
        }

    }
}
