<template>
  <div>
    <HeaderAl/>
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
  }
</script>