package cc5002.cc5002.models;
//Tuve que crear este porque le otro solo mostraba la id

import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "comuna")
public class Comuna {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer Id;
    private String nombre;
    
    public Comuna(){
    }

    public Integer getId() {
        return Id;
    }
    public String getNombre() {
        return nombre;
    }
}