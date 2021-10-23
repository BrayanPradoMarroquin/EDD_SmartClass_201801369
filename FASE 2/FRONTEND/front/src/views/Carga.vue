<template>
    <div>
        <Header/>
        <br>
        <center><h1 class="subheading grey--text">Ejecutador de Cargas</h1></center>
        <br>
        <div class="Alum_car">
            <center><h3>Carga de Alumnos</h3></center>
            <br>
            <center><p><strong>En este apartado se podra cargar a los alumnos para su posterior Registro a la Plataforma de manera independiente.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Cargar Alumnos</v-btn></center>
        </div>
        <div class="Pensum_car">
            <center><h3>Carga de Pensum</h3></center>
            <br>
            <center><p><strong>En este apartado se podrán subir los cursos pertenecientes a la escuela de Ciencias y Sistemas para asignar a los alumnos.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Cargar Pensum</v-btn></center>
        </div>
        <div class="Cursos_car">
            <center><h3>Carga de cursos</h3></center>
            <br>
            <center><p><strong>En este apartado podra subir los cursos asignados a cada alumnos registrado.</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Cargar Cursos</v-btn></center>
        </div>
        <div class="Apuntes_car">
            <center><h3>Carga de Apuntes</h3></center>
            <br>
            <center><p><strong>En este apartado podra subir los apuntes de cada curso asignado a los alumnos registrados</strong></p></center>
            <br>
            <center><v-btn color="blue" large>Cargar Apuntes</v-btn></center>
        </div>        
        <br>
        
        <Pie/>
    </div>
</template>

<script>
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'Cargas',
    components: {
      Header,
      Pie
    },
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
        top: 60%;
        padding: 2%;
        border-radius: 5%;
        box-shadow: -30px 25px 20px rgba(0, 0, 0, 0.3);
    }

    .Apuntes_car{
        background: aquamarine !important;
        width: 30%;
        position: absolute;
        left: 60%;
        top: 60%;
        padding: 2%;
        border-radius: 5%;
        box-shadow: -30px 25px 20px rgba(0, 0, 0, 0.3);
    }
</style>