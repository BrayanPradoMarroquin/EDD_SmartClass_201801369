<template>
    <div>
        <HeaderAl/>
        <center><h1 class="subheading grey--text">Gestor de Apuntes</h1></center>
        <Pie/>
    </div>
</template>

<script>
import HeaderAl from '../components/HeaderAl.vue'
import Pie from '../components/Pie.vue'
export default {
    name: 'Apuntes',
    components: {
      HeaderAl,
      Pie
    },
}
</script>