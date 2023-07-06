<script>
import Navbar from '../components/Navbar.vue'
import { ref } from 'vue';

export default {
  setup() {
    var isLogged = ref(sessionStorage.getItem('token'))
    return { isLogged }
  },
  mounted() {
    if(!this.isLogged){
      alert('You are not logged!')
      this.$router.push('login')
    }
  }
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <h1 class="title">Welcome!</h1>
    </div>
</template>