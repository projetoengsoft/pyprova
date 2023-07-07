<script>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue';

export default {
  setup() {
    var token = ref(sessionStorage.getItem('token'))
    return {
      token
    }
  },
  methods: {
    logout() {
      sessionStorage.removeItem('token');
      this.$router.push('login')
    }
  },
  // mounted(){
  //   console.log(this.token)
  // }
};
</script>

<template>
    <div class="hero-head">
        <nav class="navbar">
            <div class="container">
                <div id="navbarMenuHeroA" class="navbar-menu">
                    <div class="navbar-end">
                        <a class="navbar-item">
                            <RouterLink to="/">Home</RouterLink>
                        </a>
                        <a v-if="token" class="navbar-item">
                            <RouterLink to="/profile">Profile</RouterLink>
                        </a>
                        <a v-if="!token" class="navbar-item">
                            <RouterLink to="/login">Login</RouterLink>
                        </a>
                        <a v-if="!token" class="navbar-item">
                            <RouterLink to="/signup">Sign Up</RouterLink>
                        </a>
                        <a v-if="token" href="#" v-on:click="logout" class="navbar-item">
                            Logout
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    </div>
    <RouterView />
</template>
