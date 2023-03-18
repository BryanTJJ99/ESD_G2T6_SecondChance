package com.ESDBackend.department.models;

import java.util.ArrayList;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.Transient;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.DocumentReference;

@Document(collection = "department")
public class Department {
    
    @Id
    private String id;


    private String departmentName;

    @Transient
    private ArrayList<UserDto> users;

    private String country;

    private String postalCode;

    @Transient
    private ArrayList<ItemDto> items;

    private double totalCarbon;

    public Department() {
        // Default constructor
    }

    public Department(String departmentName, String country, String postalCode, double totalCarbon) {
        this.departmentName = departmentName;
        this.country = country;
        this.postalCode = postalCode;
        this.totalCarbon = totalCarbon;
    }
    

    //Getters and Setters
    public ArrayList<UserDto> getUsers() {
        return users;
    }

    public void setUsers(ArrayList<UserDto> users) {
        this.users = users;
    }

    public ArrayList<ItemDto> getItems() {
        return items;
    }

    public void setItems(ArrayList<ItemDto> items) {
        this.items = items;
    }



}
