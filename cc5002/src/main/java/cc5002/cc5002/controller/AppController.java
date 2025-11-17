package cc5002.cc5002.controller;

import java.util.List;
import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import cc5002.cc5002.services.AvisoService;

@Controller
public class AppController {
    private final AvisoService avisoService;
    public AppController(AvisoService avisoService){
        this.avisoService = avisoService;
    }

    //seguimos un modelo casi igual al del aux 10
    @GetMapping({"/"})
    public String listaAvisos(Model model){
        List<Map<String, String>> avisosData = avisoService.getAvisosData();
        model.addAttribute("avisos", avisosData);
        return "avisos";
    }

}
