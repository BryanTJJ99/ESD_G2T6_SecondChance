package com.ESDBackend.department.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.ESDBackend.department.models.UserDto;

public interface UserDtoRepository extends MongoRepository<UserDto, String> {
    
}
