package com.alcoyana.fabrica.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * Configuración CORS para permitir peticiones desde el frontend
 */
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")  // Permitir todas las rutas que empiecen con /api
                .allowedOrigins(
                    "http://localhost:5500",      // Live Server (VS Code)
                    "http://localhost:5501",
                    "http://127.0.0.1:5500",
                    "http://127.0.0.1:5501"
                )
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
                .allowedHeaders("*")
                .allowCredentials(true)
                .maxAge(3600);
    }
}