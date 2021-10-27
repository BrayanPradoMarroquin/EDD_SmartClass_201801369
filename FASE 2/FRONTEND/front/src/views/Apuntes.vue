<template>
    <div>
        <HeaderAl/>
        <center><h1 class="subheading grey--text">Gestor de Apuntes</h1></center>
        <div class="fo">
            <form v-on:submit.prevent="enviar">
                <label class="tit">Titulo del Apunte</label>
                <input type="text" name="" class="form-control input_user" value="" placeholder="Titulo" v-model="titulo">
                <br>
                <label class="tit">Contenido</label>
                <br>
                <textarea class="fon" v-model="contenido" rows="20" cols="80"></textarea>
                <button type="submit" name="button" class="btn_login_btn"><p>Agregar <br>Apunte</p></button>
                <button type="button" name="button" class="btn_ap_btn"><p>Ver<br> Apuntes</p></button>
            </form>
        </div>
        <Pie/>
    </div>
</template>

<script>
import HeaderAl from '../components/HeaderAl.vue'
import Pie from '../components/Pie.vue'
import axios from 'axios';
export default {
    name: 'Apuntes',
    components: {
      HeaderAl,
      Pie
    },
    data(){
		return{
			usuario: "",
			titulo: "",
			contenido: ""
		}
	},
    methods:{
        enviar(){
            let data={
                'usuario': this.$route.params.id,
                'titulo': this.titulo,
                'contenido': this.contenido
            }
            axios.post('http://localhost:3000/Apunte', data)
            .then(dato=>{
                console.log(dato)
                alert('El apunte se ha registrado con Exito')
                this.titulo=""
                this.contenido = ""
            })
        }
    }
}
</script>

<style scoped>
    .fo{
        background: aquamarine;
        width: 70%;
        height: 70%;
        position: relative;
        left: 15%;
        border-radius: 2%;
        padding: 1%;
    }
    .tit{
        font-size: 23px;
        font-family: Arial, Helvetica, sans-serif;
        position: relative;
        left: 5%;
    }
    .fon{
        position: relative;
        left: 5%;
        background: skyblue;
        width: 75%;
        height: 50%;
        border-radius: 1%;
    }
    .btn_login_btn{
        background: teal;
        padding: 2%;
        border-top-left-radius: 40%;
        border-bottom-left-radius: 10%;
        border-top-right-radius: 10%;
        border-bottom-right-radius: 40%;
        font-size: 15px;
        position: absolute;
        left: 83%;
        top: 30%;
    }
    .btn_ap_btn{
        background: teal;
        padding: 2%;
        border-top-left-radius: 40%;
        border-bottom-left-radius: 10%;
        border-top-right-radius: 10%;
        border-bottom-right-radius: 40%;
        font-size: 15px;
        position: absolute;
        left: 83%;
        top: 70%;
    }
    p{
        font-size: 25px;
    }
</style>