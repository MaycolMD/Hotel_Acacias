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
}