package cc5002.cc5002.models;

import java.time.LocalDateTime;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;

@Entity
@Table(name = "aviso_adopcion")

public class AvisoAdopcion {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private Integer id;


    @Column(name="fecha_ingreso")
    private LocalDateTime fechaIngreso;

    @NotNull
    @Column(name = "comuna_id")     //Asi aprovechamos que ya tenemos las comunas en la bdd
    private Integer comunaId;
    private String sector;

    @NotNull
    private Integer cantidad;

    @NotNull
    private String tipo;

    @NotNull
    private Integer edad;

    @NotNull
    private String unidadMedida;

    public AvisoAdopcion(){
    }

    public AvisoAdopcion(LocalDateTime fechaIngreso,
                        Integer comunaId,
                        String sector,
                        Integer cantidad,
                        String tipo,
                        Integer edad,
                        String unidadMedida){
        this.fechaIngreso = fechaIngreso;
        this.comunaId = comunaId;
        this.sector = sector;
        this.cantidad = cantidad;
        this.tipo = tipo;
        this.edad = edad;
        this.unidadMedida = unidadMedida;
    }

    
    public Integer getId(){
        return id;
    }
    public LocalDateTime getFechaIngreso(){
        return fechaIngreso;
    }
    public String getSector(){
        return sector;
    }
    public Integer getCantidad(){
        return cantidad;
    }
    public String getTipo(){
        return tipo;
    }
    public Integer getEdad(){
        return edad;
    }
    public Integer getComunaId(){
        return comunaId;
    }

    public String getUnidadMedida(){
        return unidadMedida;
    }

    
}