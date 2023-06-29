<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<script>
export default{
  data() {
    return {
      token: sessionStorage.getItem('token')
    };
  },
  methods: {
    logout() {
      sessionStorage.removeItem('token');
    }
  }
};
  var isLogged = 

  function logout(){
    sessionStorage.removeItem('token');
  }
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
                        <a v-if="isLogged !== undefined" class="navbar-item">
                            <RouterLink to="/profile">Profile</RouterLink>
                        </a>
                        <a v-if="isLogged === undefined" class="navbar-item">
                            <RouterLink to="/login">Login</RouterLink>
                        </a>
                        <a v-if="isLogged === undefined" class="navbar-item">
                            <RouterLink to="/signup">Sign Up</RouterLink>
                        </a>
                        <a v-if="isLogged !== undefined" href="#" v-on:click="logout" class="navbar-item">
                            Logout
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    </div>
    <RouterView />
</template>
