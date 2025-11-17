package cc5002.cc5002.models;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AvisoAdopcionRepository extends JpaRepository<AvisoAdopcion,Integer>{

    List<AvisoAdopcion> findAllByOrderByFechaIngresoDesc();
}
