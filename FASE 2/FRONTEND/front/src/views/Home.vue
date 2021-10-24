<template>
  <div class="home">
    <div class="container h-100">
		<br><br><br><br><br><br><br><br><br>
		<div class="d-flex justify-content-center h-100">
			<div class="user_card">
				<div class="d-flex justify-content-center">
					<div class="brand_logo_container">
						<img src="@/assets/logo.png" class="brand_logo" alt="Logo">
					</div>
				</div>
				<div class="d-flex justify-content-center form_container">
					<form v-on:submit.prevent="login">
						<div class="input-group mb-3">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-user"></i></span>
							</div>
							<input type="text" name="" class="form-control input_user" value="" placeholder="usuario" v-model="usuario">
						</div>
						<div class="input-group mb-2">
							<div class="input-group-append">
								<span class="input-group-text"><i class="fas fa-key"></i></span>
							</div>
							<input type="password" name="" class="form-control input_pass" value="" placeholder="password" v-model="password">
						</div>
						<div class="form-group">
							<div class="custom-control custom-checkbox">
								<input type="checkbox" class="custom-control-input" id="customControlInline">
								<label class="custom-control-label" for="customControlInline">Remember me</label>
							</div>
						</div>
						<div class="d-flex justify-content-center mt-3 login_container">
							<button type="submit" name="button" class="btn login_btn">Login</button>
						</div>
					</form>
				</div>
				
				<div class="mt-4">
					<div class="d-flex justify-content-center links">
						<button type="button" name="button" class="btn login_btn" v-on:click="nuevo">Registrarse</button>
					</div>
					<div class="d-flex justify-content-center links">
						<a href="#">Forgot your password?</a>
					</div>
				</div>
				<div class="alert alert-warning" role="alert" v-if="error">
					{{mensageerror}}
				</div>
			</div>
		</div>
	</div> 
	<br><br><br><br><br><br><br>   
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
export default {
	name: 'Home',
	components: {
	},
	data(){
		return{
			usuario: "",
			password: "",
			mensageerror: "",
			error: false
		}
	},
	methods:{
		login(){
			let data={
				"usuario": this.usuario,
				"password": this.password
			};
			axios.post('http://localhost:3000/Login', data)
			.then(dato=>{
				if(dato.data.status=="Yes"){
					console.log(dato)
					this.$router.push('PrincipalAlu')
				}else if(dato.data.status=="admin"){
					alert("Bienvenido usuario Admnistrador")
					this.$router.push('Principal')
				}else if(dato.data.status=="Pas"){
					this.error = true;
					this.mensageerror = "Contraseña Incorrecta";
				}else{
					this.error = true;
					this.mensageerror = "Usuario no existente";
				}
			})
		},
		nuevo(){
			this.$router.push('NewUser')
		}
	}
}
</script>

<style scoped>
	/* Coded with love by Mutiullah Samim */
		.home{
			background: #60a3bc !important;
		}
		body,
		html {
			margin: 0;
			padding: 0;
			height: 100%;
			background: #60a3bc !important;
		}
		.user_card {
			height: 400px;
			width: 350px;
			margin-top: auto;
			margin-bottom: auto;
			background: #f39c12;
			position: relative;
			display: flex;
			justify-content: center;
			flex-direction: column;
			padding: 10px;
			box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-webkit-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			-moz-box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
			border-radius: 5px;
		}
		.brand_logo_container {
			position: absolute;
			height: 170px;
			width: 170px;
			top: -75px;
			border-radius: 50%;
			background: #60a3bc;
			padding: 10px;
			text-align: center;
		}
		.brand_logo {
			height: 150px;
			width: 150px;
			border-radius: 50%;
			border: 2px solid white;
		}
		.form_container {
			margin-top: 100px;
		}
		.login_btn {
			width: 100%;
			background: #c0392b !important;
			color: white !important;
		}
		.login_btn:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.login_container {
			padding: 0 2rem;
		}
		.input-group-text {
			background: #c0392b !important;
			color: white !important;
			border: 0 !important;
			border-radius: 0.25rem 0 0 0.25rem !important;
		}
		.input_user,
		.input_pass:focus {
			box-shadow: none !important;
			outline: 0px !important;
		}
		.custom-checkbox .custom-control-input:checked~.custom-control-label::before {
			background-color: #c0392b !important;
		}
</style>