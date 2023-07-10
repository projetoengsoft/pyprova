<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: "QuestaoComponent",

  props: ['id', 'tipo', 'comando', 'opcoes', 'valor', 'gabarito', 'edit', 'resposta'],

  setup(props) {

    var mul = props.tipo === 'mul'

    var ans = props.gabarito != null

    var inputFields = ref({
      'questao': props.id,
      'resposta': props.resposta,
    })

    var data = ref({'id': props.id,
                   'tipo': props.tipo,
                   'comando': props.comando,
                   'opcoes': props.opcoes,
                   'valor': props.valor,
                   'gabarito': props.gabarito})

    return {inputFields, mul, ans, data}

  },

  methods: {
    submitAnswer(event){
        const path = `${import.meta.env.VITE_API_URL}/prova/${this.$router.params.id}/questao/${this.questao.id}/delete`;
        axios.post(path, this.inputFields, {
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
    editQuestao(event){
      this.$router.push(`/prova/${this.$router.params.id}/questao/${this.questao.id}/update`)
      event.preventDefault();
    },
    deleteQuestao(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.$router.params.id}/questao/${this.questao.id}/delete`;
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
    }
  },

}
</script>

<template>
  <div>
    <div>
      <div class="comando">{{comando}}</div>
      <div class="valor">Valor: {{valor}} pts</div>
      <div v-if="edit" class="editButtons">
        <button v-on:click="editQuestao">Edit</button>
        <button v-on:click="deleteQuestao">Delete</button>
      </div>
      <div class="resposta">
          <div v-if="mul" class="mul">
            <div class="opcao" v-for="opcao in opcoes" v-on:change="submitAnswer">
              <input type="radio" value=opcao v-model="inputFields.resposta" :disabled="edit">
              <label>{{opcao}}</label>
              <br>
            </div>
          </div>
          <div v-else-if="!edit" class="num">
            <input type="number" v-model="inputFields.resposta">
            <button v-on:click="submitAnswer">Enviar</button>
          </div>
      </div>
      <div class="gabarito" v-if="ans">
        <label>Resposta correta: {{gabarito}}</label>
        <label v-if="!edit" >Sua resposta: {{resposta}}</label>
      </div>
    </div>
  </div>
</template>
