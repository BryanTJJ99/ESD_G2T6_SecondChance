package com.ESDBackend.department.repositories;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.ESDBackend.department.models.ItemDto;

public interface ItemDtoRepository extends MongoRepository<ItemDto, String> {
    
}
