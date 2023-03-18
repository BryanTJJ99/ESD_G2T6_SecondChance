package com.ESDBackend.department.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.ESDBackend.department.models.Department;

public interface DepartmentRepository extends MongoRepository<Department, String> {
    
}
