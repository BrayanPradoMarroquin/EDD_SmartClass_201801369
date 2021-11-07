<template>
    <div>
        <HeaderAl/>
        <h1>Reporte de Prerrequisitos</h1>
        <div class="datos">
            <label class="t">Ingrese el codigo del Curso a analizar:</label><br>
            <br>
            <input type="text" name="" class="t" placeholder="Codigo" v-model="Codigo"><br>
            <br>
            <button type="button" name="button" v-on:click="enviar">Analizar</button>
        </div>
        <Pie/>
    </div>
</template>

<script>
import HeaderAl from '../components/HeaderAl.vue'
import Pie from '../components/Pie.vue'
import axios from 'axios';
export default {
    name: "Prerrequisitos",
    components: {
      HeaderAl,
      Pie,
    },
    data(){
		return{
			Codigo: ""
		}
	},
    methods:{
        enviar(){
            axios.post('http://localhost:3000/cursos?codigo='+this.Codigo)
            .then(data=>{
                console.log(data)
            })
        }
    }
}
</script>

<style scoped>
    .datos{
        border: solid 1px navy;
        width: 50%;
        position: relative;
        left: 20%;
        background-color: aqua;
        padding: 2%;
    }
    .t{
        font-size: 24px;
    }
    input{
        background-color: aliceblue;
        left: 3%;
        position: inherit;
    }
    button{
        background-color: darkblue;
        font-size: 30px;
        color: aliceblue;
        padding: 2%;
        border-radius: 30%;
        left: 50%;
        position: inherit;
    }
</style>