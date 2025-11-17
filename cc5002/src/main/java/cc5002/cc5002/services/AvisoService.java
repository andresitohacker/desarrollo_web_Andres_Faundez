package cc5002.cc5002.services;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import cc5002.cc5002.models.AvisoAdopcion;
import cc5002.cc5002.models.AvisoAdopcionRepository;
import cc5002.cc5002.models.Nota;
import cc5002.cc5002.models.NotaRepository;
import cc5002.cc5002.models.Comuna;
import cc5002.cc5002.models.ComunaRepository;

import org.springframework.stereotype.Service;

@Service
public class AvisoService {
    private final AvisoAdopcionRepository avisoAdopcionRepository;
    private final NotaRepository notaRepository;
    private final ComunaRepository comunaRepository;

    public AvisoService(AvisoAdopcionRepository avisoAdopcionRepository, NotaRepository notaRepository, ComunaRepository comunaRepository){
        this.avisoAdopcionRepository = avisoAdopcionRepository;
        this.notaRepository = notaRepository;
        this.comunaRepository = comunaRepository;
    }

    //Aca calculmaos el promedio
    public Double promedioNota(Integer avisoId){
        List<Nota> notas = notaRepository.findByAvisoId(avisoId);

        if (notas.isEmpty()){
            return null;
        }

        return notas.stream()
                    .mapToInt(Nota::getNota)
                    .average()
                    .orElse(0.0); //Sin esta linea no se por que me daba error de mismatch
    }
    //Falta la logica de al agregar una nueva nota actualizar
    public Double nuevaNota(Integer avisoId, Integer nota){
        Nota nueva = new Nota(avisoId, nota);
        notaRepository.save(nueva);               
        return promedioNota(avisoId);
    }
    //Avisos ordenados por orden de subida
     public List<AvisoAdopcion> avisos(){
        return avisoAdopcionRepository.findAllByOrderByFechaIngresoDesc();
     }


     public List<Map<String,String>> getAvisosData(){
        List<AvisoAdopcion> avisos = avisos();
        List<Map<String,String>> data = new ArrayList<>();

        for (AvisoAdopcion aviso : avisos){
            Map<String,String> avisoData = new HashMap<>();
            avisoData.put("id", aviso.getId().toString());
            avisoData.put("fecha_publicacion", aviso.getFechaIngreso().toString());
            avisoData.put("sector", aviso.getSector());
            avisoData.put("cantidad", aviso.getCantidad().toString());
            avisoData.put("tipo", aviso.getTipo());
            avisoData.put("edad", aviso.getEdad().toString());
            avisoData.put("unidad_medida", aviso.getUnidadMedida());
            
            if (aviso.getComunaId() != null){
                String nombreComuna = comunaRepository.findById(aviso.getComunaId())
                                        .map(Comuna::getNombre)
                                        .orElse("Desconocida");
                avisoData.put("comuna", nombreComuna);
            }

            Double promedio = promedioNota(aviso.getId());
            if (promedio != null){
                double redondeado = Math.round(promedio * 10) / 10.0;
                avisoData.put("nota", Double.toString(redondeado));
            }else{
                avisoData.put("nota", "-");
            }
            data.add(avisoData);
        }

        return data;
     }
}
