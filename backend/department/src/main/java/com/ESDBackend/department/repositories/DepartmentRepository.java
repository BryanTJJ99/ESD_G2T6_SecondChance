package com.ESDBackend.department.repositories;

import java.util.Optional;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.ESDBackend.department.models.Department;

public interface DepartmentRepository extends MongoRepository<Department, String> {
    Optional<Department> findByEmail(String email);

    Optional<Department> findByDepartmentNameAndPostalCode(String departmentName, String postalCode);
}
