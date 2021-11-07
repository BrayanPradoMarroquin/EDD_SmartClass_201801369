<template>
    <div>
        <Header/>
        <center>
            <h1>Malla Curricular de Ingenieria en Ciencias y Sistemas</h1>
        </center>
        <center>
            <v-img src="../assets/Pensum.png" class="ajusteE"></v-img>
        </center>
        <Pie/>
    </div>
</template>

<script>
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'ReportePensum',
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