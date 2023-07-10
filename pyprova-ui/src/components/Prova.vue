<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: "ProvaComponent",

  props: ['id', 'inicio', 'fim', 'edit'],

  setup(props) {

    var data = ref({'id': props.id,
                   'inicio': props.inicio,
                    'fim': props.fim
                    })

    return {data}

  },

  methods: {
    updateProva(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.$router.params.id}/update`;
        axios.post(path, this.data, {
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
    deleteProva(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.$router.params.id}/delete`;
        axios.post(path, this.data, {
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
  },

}
</script>

<template>
  <div>
    <div>
      <router-link to="/prova/${data.id}">{{data.id}}</router-link>
      <label>Inicio: <input type="datetime-local" v-model="data.inicio" :disabled="!edit" v-on:input="updateProva"></label>
      <label>Fim: <input type="datetime-local" v-model="data.fim" :disabled="!edit" v-on:input="updateProva"></label>
      <div v-if="edit" class="editButtons">
        <button v-on:click="deleteProva">Delete</button>
      </div>
    </div>
  </div>
</template>
