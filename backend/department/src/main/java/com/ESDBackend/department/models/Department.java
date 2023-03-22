package com.ESDBackend.department.models;

import java.util.ArrayList;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.Transient;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "department")
public class Department {
    
    @Id
    private String departmentId;


    private String departmentName;


    private String departmentCountry;

    private String departmentPostalCode;

    @Transient
    private ArrayList<String> items;

    private double totalCarbon;

    // public Department() {
    //     // Default constructor
    // }
    public Department(String departmentName, String country, String postalCode, double totalCarbon) {
        this.departmentName = departmentName;
        this.departmentCountry = country;
        this.departmentPostalCode = postalCode;
        this.totalCarbon = totalCarbon;
        this.items = new ArrayList<String>();
    }
    

    //Getters and Setters

    public ArrayList<String> getItems() {
        return items;
    }

    
    public void addItem(String itemID){
        items.add(itemID);
    }
    

    public void removeItem(String itemID){
        items.remove(itemID);
    }


}


