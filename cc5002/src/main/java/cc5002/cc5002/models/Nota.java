package cc5002.cc5002.models;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;


@Entity
@Table(name= "nota")

public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    
    @NotNull
    @Column(name = "aviso_id")
    private Integer avisoId;

    @NotNull
    private Integer nota;

    public Nota(){
    }

    public Nota(Integer avisoId, Integer nota){
        this.avisoId = avisoId;
        this.nota = nota;
    }
    public Integer getId(){
        return id;
    }
    public Integer getAvisoId(){
        return avisoId;
    }
    public Integer getNota(){
        return nota;
    }

}
