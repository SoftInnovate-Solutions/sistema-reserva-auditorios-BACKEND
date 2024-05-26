from datetime import datetime, timedelta

class Generador():
    def generadorSql(filtro: tuple):
        sql = 'SELECT a.cod_ambiente, a.nombre_amb, e.nombre_ea, a.capacidad_amb From ambiente a JOIN estado_ambiente e ON a.cod_estado_ambiente = e.cod_estado_ambiente'
        if not all(e == -1 for e in filtro):
            where = ' WHERE '
            sql += where
            p1 = p2 = p3 = p4 = ''
            if filtro[0] != -1:
                p1 = 'a.cod_tipo_ambiente = %s' % filtro[0]
            if filtro[1] != -1:
                p2 = 'a.cod_facultad = %s' % filtro[1]
            if filtro[2] != -1:
                p3 = 'a.cod_edificacion = %s' % filtro[2]
            if filtro[3] != -1:
                p4 = 'a.cod_estado_ambiente = %s' % filtro[3]
            sql += (p1 if p1 != '' else '') +(' AND ' if p1 != '' and (p2 != '' or p3 != '' or p4 != '') else '') \
            + (p2 if p2 != '' else '') + (' AND ' if p2 != '' and (p3 != '' or p4 != '') else '') \
            + (p3 if p3 != '' else '') + (' AND ' if p3 != '' and p4 != '' else '')  + (p4 if p4 != '' else '')
        return sql + ';'

    def generar_dias(configuracion):
        configuracion_transpuesta = [[fila[i] for fila in configuracion] for i in range(len(configuracion[0]))]
        dia = 1
        dias = []
        for columna in configuracion_transpuesta:
            if 1 in columna:
                dias.append(dia)
            dia += 1
        return dias

    def generar_dia_bloques(dias,configuracion):
        dia_bloques = {}
        bloques = []
        for dia in dias:
            i = 1
            for seleccioando in configuracion:
                if seleccioando[dia-1] == 1:
                    bloques.append(i)
                i += 1
            dia_bloques[dia] = bloques
            bloques = []
        
        return dia_bloques

    def generar_ajustes(desde, hasta, dia_bloques):
        fecha_inicio = datetime.strptime(desde, '%Y-%m-%d')
        fecha_fin = datetime.strptime(hasta, '%Y-%m-%d')
        ajustes = []
        for dia, bloques in dia_bloques.items():
            for bloque in bloques:
                while fecha_inicio <= fecha_fin:
                    if fecha_inicio.isoweekday() == dia:
                        ajustes.append((dia,bloque,fecha_inicio.strftime('%Y-%m-%d')))
                    fecha_inicio += timedelta(days=1)
                fecha_inicio = datetime.strptime(desde, '%Y-%m-%d')
        return ajustes
    
    def generar_configuracion(dias, bloques):
        dias = [d[0] for d in dias]
        bloques = [b for b in bloques]
        bloquesRefinados = {}
        for dia in dias:
            if dia not in bloquesRefinados:
                bloquesRefinados[dia] = []

        for a, b in bloques:
            bloquesRefinados[a].append(b)

        configuracion_transpuesta = []

        for dia in range(1,8):
            parametro = []
            if dia in bloquesRefinados:
                lista = bloquesRefinados[dia]
                for bloque in range(1,11):
                    parametro.append(1 if bloque in lista else 0)
            else:
                parametro = [0]*10
            configuracion_transpuesta.append(parametro)

        configuracion = [[fila[i] for fila in configuracion_transpuesta] for i in range(len(configuracion_transpuesta[0]))]

        return configuracion



        
            

