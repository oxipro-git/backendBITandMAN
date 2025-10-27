COLUMNAS_MANTENIMIENTO = [
    # --- Identificación general ---
    "fecha_registro",
    "nombre_tecnico",
    "sede",
    "equipo",
    "codigo_interno",
    "area",
    "ubicacion",
    "estado_general",  # aprobado / inspeccion / pendiente / tercero

    # --- Datos del mantenimiento ---
    "tipo_mantenimiento",  # preventivo / correctivo / predictivo
    "hora_inicio",
    "hora_fin",
    "tiempo_total",
    "actividad_realizada",
    "observaciones_generales",

    # --- Resultados / condición del equipo ---
    "condiciones_iniciales",
    "condiciones_finales",
    "repuestos_utilizados",
    "cantidad_repuestos",
    "estado_repuesto",  # nuevo / reparado / sin cambio
    "seguimiento_requerido",  # sí / no
    "detalle_seguimiento",

    # --- Validación / control ---
    "firma_tecnico",
    "firma_supervisor",
    "observaciones_supervisor",

    # --- Bloque de novedad 1 ---
    "novedad1_tipo",
    "novedad1_descripcion",
    "novedad1_accion_tomada",
    "novedad1_responsable",

    # --- Bloque de novedad 2 ---
    "novedad2_tipo",
    "novedad2_descripcion",
    "novedad2_accion_tomada",
    "novedad2_responsable",

    # --- Bloque de novedad 3 ---
    "novedad3_tipo",
    "novedad3_descripcion",
    "novedad3_accion_tomada",
    "novedad3_responsable",

    # --- Campos administrativos ---
    "fecha_programada",
    "prioridad",  # alta / media / baja
    "requiere_tercero",  # sí / no
    "nombre_tercero",
    "estado_tercero",  # en curso / completado / pendiente
    "observaciones_finales",
]
