<template>
    <div>
        <Header/>
        <h1>Reporte de Alumnos Inscritos</h1>
        <center>
            <div>
            <div class="encryp">
                <center>
                    <v-img src="../assets/ArbolAVLEncrypt_Alumnos.png" class="ajusteE"></v-img>
                </center>
            </div>
            <br><br><br><br><br>
            <div class="decryp">
                <center>
                    <v-img src="../assets/ArbolAVLDecrypt_Alumnos.png" class="ajuste"></v-img>    
                </center>
            </div>
        </div>
        </center>
        <Pie/>
    </div>
</template>

<script>
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'ReporteAlumnos',
    components: {
      Header,
      Pie
    }
}
</script>

<style scoped>
    .ajuste{
        height: 70%;
        width: 70%;
    }
    .ajusteE{
        height: 100%;
        width: 65%;
    }
    .encryp{
        border-radius: 25%;
        padding-bottom: 1%;
        padding-top: 1%;
        border: 1px solid black;
        width: 90%;
    }
    .decryp{
        border-radius: 10%;
        border: 1px solid black;
        height: 50%;
        width: 90%;
    }
</style>