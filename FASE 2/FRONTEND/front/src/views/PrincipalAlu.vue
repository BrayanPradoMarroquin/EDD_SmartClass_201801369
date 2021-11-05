<template>
    <div>
        <HeaderAl/>
        <br>
        <center><h1 class="subheading grey--text">PRINCIPAL - ALUMNOS</h1></center>
        <br>
        <div class="Alum_car">
            <center><h3>Apuntes</h3></center>
            <br>
            <center><p><strong>En este apartado se podra registrar apuntes y observar los mismo.</strong></p></center>
            <br>
            <center><v-btn color="blue" large v-on:click="Apunt">Ir a Apuntes</v-btn></center>
        </div>
        <div class="Pensum_car">
            <center><h3>Asignar Cursos</h3></center>
            <br>
            <center><p><strong>En este apartado se podra asignar a los cursos del Pensum de Ciencias y Sistemas.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Curso</v-btn></center>
        </div>
        <div class="Cursos_car">
            <center><h3>Reporte de Prerrequisitos</h3></center>
            <br>
            <center><p><strong>Reporte generado para observar los Prerrequisitos del curso solicitado.</strong></p></center>
            <br>
            <center><v-btn color="blue" large v-on:click="Report">Generar Reporte</v-btn></center>
        </div>
        <div class="Apuntes_car">
            <center><h3>Reporte de Cursos otro</h3></center>
            <br>
            <center><p><strong>Reporte generado de cursos asignados por el estudiante para el semestre dado.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Generar Apuntes</v-btn></center>
        </div>        
        <br>
        
        <Pie/>
    </div>
</template>

<script>
import HeaderAl from '../components/HeaderAl.vue'
import Pie from '../components/Pie.vue'
  export default {
    name: 'PrincipalAlu',
    components: {
      HeaderAl,
      Pie
    },
    methods:{
        Apunt(){
            this.$router.push('/Apuntes/'+this.$route.params.id)
        },
        Report(){
            this.$router.push('/Prerrequisitos/'+this.$route.params.id)
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