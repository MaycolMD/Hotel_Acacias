export default class API{
    url ="http://127.0.0.1:5000/api/";
    async getReservasActivas() {
        const path = `${this.url}reservasActivas`;
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();
    }
    async getReservas() {
        const path = `${this.url}reservas`;
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();
    }
    async getParos() {
        const path = `${this.url}paros`;
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();
    }
    async getHuespedes() {
        const path = `${this.url}huespedes`;
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();
    }
    async getHabitaciones(type,startDate,endDate,adults,kids,babies,hab) {
        const path = `${this.url}buscador?tipo=${type}&fechaInicio=${startDate}&fechaFin=${endDate}&adultos=${adults}&niños=${kids}&bebes=${babies}&habitaciones=${hab}`
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();
    }
    async assignID(fechaInicio,fechaFin,tipo) {
        const path = `${this.url}obtenerid?fechaInicio=${fechaInicio}&fechaFin=${fechaFin}&tipo=${tipo}`
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();        
    }
    async reservar(tipo,fechaInicio,fechaFin,habitaciones,id_cliente,id_hab,nacionalidad,origen,nombres,apellidos) {
        const path = `${this.url}reservar?fechaInicio=${fechaInicio}&fechaFin=${fechaFin}&tipo=${tipo}&habitaciones=${habitaciones}&id_cliente=${id_cliente}&id_hab=${id_hab}&nacionalidad=${nacionalidad}&origen=${origen}&nombres=${nombres}&apellidos=${apellidos}`
        const options = {
            headers: {
              Accept: 'application/json'
            }
        };
        const response = await fetch(path,options)
        return response.json();     
    }
}