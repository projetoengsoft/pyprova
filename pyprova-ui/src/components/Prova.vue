<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: "ProvaComponent",

  props: ['id', 'inicio', 'fim', 'edit'],
  emits:  ['delete'],

  setup(props) {


    var data = ref({'id': props.id,
                   'inicio': props.inicio,
                    'fim': props.fim,
                    })

    return {data}

  },

  methods: {
    viewProva(event){
      this.$router.push({name: 'provaView', params: {id: this.data.id}})
      event.preventDefault();
    },
    updateProva(event){
      const path = `${import.meta.env.VITE_API_URL}prova/${this.id}/update`;
        axios.post(path, this.data, {
        headers:{
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
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
      const path = `${import.meta.env.VITE_API_URL}prova/${this.id}/delete`;
        axios.post(path, this.data, {
        headers:{
          'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){ this.$emit('delete') } else {
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
      <a v-on:click="viewProva" class="button">Código: {{data.id}}</a>
      <label>Inicio: <input type="datetime-local" v-model="data.inicio" :disabled="!edit" v-on:input="updateProva"></label>
      <label>Fim: <input type="datetime-local" v-model="data.fim" :disabled="!edit" v-on:input="updateProva"></label>
      <div v-if="edit" class="editButtons">
        <button v-on:click="deleteProva">Delete</button>
      </div>
    </div>
  </div>
</template>
