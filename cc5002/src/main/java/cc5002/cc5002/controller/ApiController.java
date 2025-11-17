package cc5002.cc5002.controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import cc5002.cc5002.services.AvisoService;
@RestController
public class ApiController {
    private final AvisoService avisoService;
    public ApiController(AvisoService avisoService){
        this.avisoService = avisoService;
    }

    @PostMapping("/api/evaluar")
    public String evaluarAviso(
        @RequestParam("aviso_id") Integer avisoId,
        @RequestParam("nota") Integer nota){
            Double nuevoProm = avisoService.nuevaNota(avisoId, nota);

            if (nuevoProm == null){
                return "-";
            }
            double redondeado = Math.round(nuevoProm * 10) / 10.0;
            return Double.toString(redondeado);
        }
    
    


}
