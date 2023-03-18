package com.ESDBackend.department.models;

public class ItemDto {

    private String id;

    private String itemName;

    private String category;

    public ItemDto() {
        // Default constructor
    }

    public ItemDto(String id, String itemName, String category) {
        this.id = id;
        this.itemName = itemName;
        this.category = category;
    }

    //Getters and Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getItemName() {
        return itemName;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    // Getters and setters for all fields
}