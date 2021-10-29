import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Principal from '../views/Principal.vue'
import NewUser from '../views/NewUser.vue'
import Carga from '../views/Carga.vue'
import Report from '../views/Report.vue'
import PrincipalAlu from '../views/PrincipalAlu.vue'
import Apuntes from '../views/Apuntes.vue'
import ReporteAlumnos from '../views/ReporteAlumnos.vue'
import ReporteHash from '../views/ReporteHash.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Principal',
    name: 'Principal',
    component: Principal
  },
  {
    path: '/PrincipalAlu/:id',
    name: 'PrincipalAlu',
    component: PrincipalAlu
  },
  {
    path: '/NewUser',
    name: 'NewUser',
    component: NewUser
  },
  {
    path: '/Carga',
    name: 'Carga',
    component: Carga
  },
  {
    path: '/Report',
    name: 'Report',
    component: Report
  },
  {
    path: '/Apuntes/:id',
    name: 'Apuntes',
    component: Apuntes 
  },
  {
    path: '/ReporteAlumnos',
    name: 'ReporteAlumnos',
    component: ReporteAlumnos
  },
  {
    path: '/ReporteHash',
    name: 'ReporteHash',
    component: ReporteHash
  }
]

const router = new VueRouter({
  routes
})

export default router
