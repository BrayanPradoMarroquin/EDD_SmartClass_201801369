<template>
    <div>
        <Header/>
        <center>
            <h1>Reporte de Apuntes por Alumnos</h1>
        </center>
        <center>
            <v-img src="../assets/TablaHash.png" class="ajusteE"></v-img>
        </center>
        <Pie/>
    </div>
</template>

<script>
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'ReporteHash',
    components: {
      Header,
      Pie
    }
}
</script>

<style scoped>
    .ajusteE{
        width: 100%;
    }
</style>