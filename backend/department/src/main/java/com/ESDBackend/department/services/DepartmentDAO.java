package com.ESDBackend.department.services;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Service;
import java.util.*;
import com.ESDBackend.department.models.*;


@Service
public class DepartmentDAO {

    @Autowired
    private MongoTemplate mongoTemplate;

    public int addItem(String departmentID, String itemID) {
        // Check if the item already exists in the database
        try {
            Department dept = mongoTemplate.findById(departmentID, Department.class);
            dept.addItem(itemID);
            mongoTemplate.save(dept);
            
            // 0 for success
            return 0;
        } catch (Exception e) {
            System.out.println(e.getMessage());

            //-1 for unsuccessful attempt
            return -1;
        }
        
        
    }

    public ArrayList<String> getDepartmentItems(String departmentId) {
        try {
            Department dept = mongoTemplate.findById(departmentId, Department.class);
            return dept.getItems();
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return null;
        }
    }

    public int removeItem(String departmentID, String itemID) {
        // Find the item in the database

        try {
            Department dept = mongoTemplate.findById(departmentID, Department.class);
            dept.removeItem(itemID);
            mongoTemplate.save(dept);

            return 0;
        } catch (Exception e) {
            // TODO: handle exception
            System.out.println(e.getMessage());
            return -1;

        }
       
    }

    public int itemTransfer(Department sendingDepartment, Department receivingDepartment, String itemID) {
        return -1;
    }
}
