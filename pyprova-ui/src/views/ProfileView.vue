<script>
import Navbar from '../components/Navbar.vue'
import { ref } from 'vue';
import axios from 'axios';
import jwtDecoder from '../utils/jwtDecoder';
import ProvaComponent from "../components/Prova.vue";

export default {
  components: {ProvaComponent},
  setup() {
    var info = {data:{}};
    const renderComponent = ref(true);
    info.codigo=null
    info.inicio = null
    info.fim = null
    var isLogged = ref(sessionStorage.getItem('token'))
    return { isLogged, info, renderComponent }
  },
  mounted() {
    if (!this.isLogged) {
      alert('You are not logged!')
      this.$router.push('login')
    } else {
      console.log(jwtDecoder(this.isLogged, 'sub'));
    }
    this.get()
  },
  methods: {
    async get() {
      const path = `${import.meta.env.VITE_API_URL}`;
      var request = {
      headers: {
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
      }
    }
    this.info.data = await axios.get(path, request)
        .then(response => {
          if (response.data.success) {
            this.forceRender()
            return response.data.message
          } else {
            throw new Error(response.data.message)
          }
        })
        .catch((err) => {
          alert(err);
        });
    },
    async forceRender() {
   // Remove MyComponent from the DOM
   this.renderComponent = false;

   // Then, wait for the change to get flushed to the DOM
      await this.$nextTick();

      // Add MyComponent back in
      this.renderComponent = true;
    },
    addProva(event){
      if (this.info.inicio !== null && this.info.fim !== null){
      const path = `${import.meta.env.VITE_API_URL}/prova/0/create`;
      var data = {
        inicio: this.info.inicio,
        fim: this.info.fim
      }
        axios.post(path, data, {
        headers:{
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){
          this.get()
        } else {
          throw new Error(res.data.message)
        }
      })
      .catch((err) => {
        alert(err);
      });
      event.preventDefault();
    }
      else {
        alert('Preencha os campos')
      }
      },
    registerProva(event){
      if (this.info.codigo !== null){
      const path = `${import.meta.env.VITE_API_URL}prova/${this.info.codigo}/register`;
      var data = {
        inicio: null,
        fim: null
      }
        axios.post(path, data, {
        headers:{
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){
          alert(res.data.message)
          this.get()
        } else {
          throw new Error(res.data.message)
        }
      })
      .catch((err) => {
        alert(err);
      });
      event.preventDefault();
    }
    else {
      alert("Insira um codigo")
    }}
  }
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <h1 class="title">Suas Provas</h1>
      <div v-if="renderComponent" class="column is-4 is-offset-4">
        <ul>
          <li v-for="prova in info.data.provas" v-bind:key="prova">
            <ProvaComponent @delete="get" v-bind="prova" v-bind:edit="info.data.edit"/>
          </li>
        </ul>
        <div v-if="renderComponent">
        <div v-if="info.data.edit === true" class="adicionarProva">
          <label>Inicio: <input type="datetime-local" v-model="info.inicio"></label>
          <label>Fim: <input type="datetime-local" v-model="info.fim"></label>
          <button  v-on:click="addProva">Adicionar Prova</button>
        </div>
        <div v-else class="registrarProva">
          <label>Codigo <input type="number" v-model="info.codigo"></label>
          <button v-on:click="registerProva">Registrar Prova</button>
        </div></div>
      </div>
    </div>
</template>