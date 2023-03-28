package com.ESDBackend.department.models;

import java.util.ArrayList;
import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;


import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Document(collection = "departments")
public class Department {
    
    @Id
    private String departmentId;
    private String departmentName;
    private String companyId;
    private String email;
    private List<String> itemIdArrayList;
    private String password;
    private String postalCode;
    private double totalCarbon;
    

    // public Department() {
    //     // Default constructor
    // }
    // public Department(String departmentName, String country, String postalCode, double totalCarbon) {
    //     this.departmentName = departmentName;
    //     this.departmentCountry = country;
    //     this.departmentPostalCode = postalCode;
    //     this.totalCarbon = totalCarbon;
    //     this.itemIdArrayList = new ArrayList<String>();
    // }
    
    public Department() {

    }


    // public List<String> getItemsIdArr() {
    //     return itemIdArrayList;
    // }

    
    public void addItem(String itemID){
        itemIdArrayList.add(itemID);
    }
    

    public void removeItem(String itemID){
        itemIdArrayList.remove(itemID);
    }


}


