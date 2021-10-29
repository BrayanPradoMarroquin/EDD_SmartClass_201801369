<template>
    <div>
        <Header/>
        <br>
        <center><h1 class="subheading grey--text">Ejecutador de Reportes</h1></center>
        <br>
        <div class="Alum_car">
            <center><h3>Alumnos</h3></center>
            <br>
            <center><p><strong>Reporte generado para observar los datos de los alumnos registrados en la plataforma.</strong></p></center>
            <br>
            <center><v-btn color="blue" large v-on:click="Alumnos">Generar Alumnos</v-btn></center>
        </div>
        <div class="Pensum_car">
            <center><h3>Prerrequisitos de Cursos</h3></center>
            <br>
            <center><p><strong>Reporte generado para observar los prerrequisitos de los cursos asignados.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Curso</v-btn></center>
        </div>
        <div class="Cursos_car">
            <center><h3>Arbol de Merkle</h3></center>
            <br>
            <center><p><strong>Reporte generado para observar el comportamiento de los bloques generados.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Generar Arbol</v-btn></center>
        </div>
        <div class="Apuntes_car">
            <center><h3>Apuntes</h3></center>
            <br>
            <center><p><strong>Reporte generado para observar los apuntes de los alumnos registrados.</strong></p></center>
            <br>
            <center><v-btn color="blue" large v-on:click="Apuntes">Generar Apuntes</v-btn></center>
        </div>        
        <br>
        
        <Pie/>
    </div>
</template>

<script>
import axios from 'axios';
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'Report',
    components: {
      Header,
      Pie
    },
    methods:{
        Alumnos(){
            let data = {
                'tipo': "0"
            };
            axios.post('http://localhost:3000/reporte', data)
            .then(data=>{
                console.log(data)
                this.$router.push('/ReporteAlumnos')
            })
        },
        Apuntes(){
            let data = {
                'tipo': "1"
            };
            axios.post('http://localhost:3000/reporte', data)
            .then(data=>{
                console.log(data)
                this.$router.push('/ReporteHash')
            })
        }
    }
}
</script>

<style scoped>
    .Alum_car{
        background: aquamarine !important;
        width: 30%;
        position: absolute;
        left: 10%;
        padding: 2%;        
        border-radius: 5%;
        box-shadow: 30px -25px 20px rgba(0, 0, 0, 0.3);
    }

    .Pensum_car{
        background: aquamarine !important;
        width: 30%;
        position: absolute;
        left: 60%;
        padding: 2%;
        border-radius: 5%;
        box-shadow: 30px -25px 20px rgba(0, 0, 0, 0.3);
    }

    .Cursos_car{
        background: aquamarine !important;
        width: 30%;
        position: absolute;
        left: 10%;
        top: 57%;
        padding: 2%;
        border-radius: 5%;
        box-shadow: -30px 25px 20px rgba(0, 0, 0, 0.3);
    }

    .Apuntes_car{
        background: aquamarine !important;
        width: 30%;
        position: absolute;
        left: 60%;
        top: 57%;
        padding: 2%;
        border-radius: 5%;
        box-shadow: -30px 25px 20px rgba(0, 0, 0, 0.3);
    }
</style>