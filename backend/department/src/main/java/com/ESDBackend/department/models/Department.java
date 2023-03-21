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
    private ArrayList<ItemDto> items;

    private double totalCarbon;

    // public Department() {
    //     // Default constructor
    // }
    public Department(String departmentName, String country, String postalCode, double totalCarbon) {
        this.departmentName = departmentName;
        this.country = country;
        this.postalCode = postalCode;
        this.totalCarbon = totalCarbon;
        this.items = new ArrayList<ItemDto>();
    }
    

    //Getters and Setters

    public ArrayList<String> getItems() {
        return items;
    }

    
    public void addItem(ItemDto item){
        items.add(item);
    }
    

    public void removeItem(ItemDto item){
        items.remove(item);
    }


}


