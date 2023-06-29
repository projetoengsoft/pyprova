<script setup>
import { RouterLink, RouterView } from 'vue-router';
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
                        <a class="navbar-item">
                            <RouterLink to="/profile">Profile</RouterLink>
                        </a>
                        <a class="navbar-item">
                            <RouterLink to="/login">Login</RouterLink>
                        </a>
                        <a class="navbar-item">
                            <RouterLink to="/signup">Sign Up</RouterLink>
                        </a>
                        <a href="#" class="navbar-item">
                            Logout
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    </div>
    <RouterView />
</template>
