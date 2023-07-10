<script>
import Navbar from '../components/Navbar.vue'
import { ref } from 'vue';
import axios from "jsdom/lib/jsdom/living/fetch/header-list";
import ProvaComponent from "../components/Prova";

export default {
  components: {ProvaComponent},
  setup() {
    var info = {}
    const path = `${import.meta.env.VITE_API_URL}`;
    axios.get(path)
        .then(response => {
          if (response.data.success) {
            this.info = response.data.message
          } else {
            throw new Error(response.data.message)
          }
        })
        .catch((err) => {
          alert(err);
        });

    info.codigo=-1
    var isLogged = ref(sessionStorage.getItem('token'))
    return { isLogged, info }
  },
  mounted() {
    if(!this.isLogged){
      alert('You are not logged!')
      this.$router.push('login')
    }
  },
  methods: {
    addProva(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/0/create`;
      var data = ref({
        'inicio': this.info.inicio,
        'fim': this.info.fim
      })
        axios.post(path, data, {
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){ /* empty */ } else {
          throw new Error(res.data.message)
        }
      })
      .catch((err) => {
        alert(err);
      });
      event.preventDefault();
    },
    registerProva(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.info.codigo}/register`;
      var data = ref({
        'inicio': null,
        'fim': null
      })
        axios.post(path, data, {
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){ /* empty */ } else {
          throw new Error(res.data.message)
        }
      })
      .catch((err) => {
        alert(err);
      });
      event.preventDefault();
    }
  }
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <h1 class="title">Suas Provas</h1>
      <div class="provas">
        <ul>
          <li v-for="prova in info.provas" v-bind:key="prova">
            <ProvaComponent v-bind="prova"/>
          </li>
        </ul>
        <div v-if="info.edit" class="adicionarProva">
          <label>Inicio: <input type="datetime-local" v-model="info.inicio"></label>
          <label>Fim: <input type="datetime-local" v-model="info.fim"></label>
          <button  v-on:click="addProva">Adicionar Prova</button>
        </div>
        <div v-else class="registrarProva">
          <label>Codigo <input type="number" v-model="info.codigo"></label>
          <button v-on:click="registerProva">Registrar Prova</button>
        </div>
      </div>
    </div>
</template>