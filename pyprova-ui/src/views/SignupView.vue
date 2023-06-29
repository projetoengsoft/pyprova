<script setup>
import Navbar from '../components/Navbar.vue'
</script>

<script>
  import axios from 'axios';

  var inputFields = {
    email: '',
    name: '',
    password: ''
  }

  function getFields(event){
    const path = `${import.meta.env.VITE_API_URL}signup`;
    axios.post(path, inputFields, {
      headers:{
        'Content-Type': 'application/json'
      }
    })
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
    event.preventDefault();
  }
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <div class="column is-4 is-offset-4">
            <h3 class="title">Sign Up</h3>
            <div class="box">
                <form>
                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="email" 
                          placeholder="Email" autofocus="" v-model="inputFields.email">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="text"
                          placeholder="Name" autofocus="" v-model="inputFields.name"> 
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="password"
                          placeholder="Password" v-model="inputFields.password">
                        </div>
                    </div>

                    <button v-on:click="getFields" class="button is-block is-info is-large is-fullwidth">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
</template>