<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: "QuestaoComponent",

  props: ['id', 'tipo', 'comando', 'opcoes', 'valor', 'gabarito', 'edit', 'resposta', 'correct', 'done'],
  emits:  ['delete'],

  setup(props) {

    var mul = props.tipo === 'mul' || props.tipo === 'vf'


    var inputFields = {
      'resposta': props.resposta,
    }

    var data = ref({'id': props.id,
                   'tipo': props.tipo,
                   'comando': props.comando,
                   'opcoes': props.opcoes,
                   'valor': props.valor,
                   'gabarito': props.gabarito})

    return {inputFields, mul, data}

  },

  methods: {
    submitAnswer(event){
      if (this.inputFields.resposta != null) {
        const path = `${import.meta.env.VITE_API_URL}/prova/${this.$route.params.id}/questao/${this.data.id}/responder`;
        axios.post(path, this.inputFields, {
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
    }},
    editQuestao(event){
      this.$router.push(`/prova/${this.$route.params.id}/questao/${this.data.id}/update`)
      event.preventDefault();
    },
    deleteQuestao(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.$route.params.id}/questao/${this.data.id}/delete`;
      axios.post(path, this.data, {
        headers:{
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
    }
  },

}
</script>

<template>
  <div>
    <div>
      <div class="comando">{{comando}}</div>
      <div class="valor">Valor: {{valor}} pts</div>
      <div v-if="edit&&!(done)" class="editButtons">
        <button v-on:click="editQuestao">Edit</button>
        <button v-on:click="deleteQuestao">Delete</button>
      </div>
      <div class="resposta">
          <div v-if="mul" class="mul">
            <div class="opcao" v-for="opcao in opcoes" v-on:change="submitAnswer">
              <input :name="'escolha_' + this.id" type="radio" :value="opcao" v-model="inputFields.resposta" :disabled="edit||done">
              <label>{{opcao}}</label>
              <br>
            </div>
          </div>
          <div v-else-if="!edit" class="num">
            <input type="number" v-model="inputFields.resposta" :disabled="edit||done">
            <button v-if="!(edit||done)" v-on:click="submitAnswer">Enviar</button>
          </div>
      </div>
      <div class="gabarito" v-if="done">
        <div v-if="correct">
          <label> Resposta Correta!</label>
        </div>
        <div v-else>
          <label>Resposta correta: {{gabarito}}</label>
          <br>
        <label v-if="!edit" >Sua resposta: {{resposta}}</label>
        </div>
      </div>
    </div>
  </div>
</template>
