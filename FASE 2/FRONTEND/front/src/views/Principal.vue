<template>
  <div>
    <Header/>
    <Pie/>
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Pie from '../components/Pie.vue'
  export default {
    name: 'Principal',

    components: {
      Header,
      Pie
    },
  }
</script>
