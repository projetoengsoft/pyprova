<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: "QuestaoView",
  setup() {
    var update = this.$route.params.method === 'update'

    var questao = ref({'id': '',
                   'tipo': '',
                   'comando': '',
                   'opcoes': [],
                   'valor': 1,
                   'gabarito': ''})

    if (update) {
    const path = `${import.meta.env.VITE_API_URL}/prova/${this.$route.params.id}/questao/${this.$route.params.questao_id}/detail`;
    axios.get(path)
        .then(response => {
          if (response.data.success) {
            this.info = response.data.message
            this.questao.id = this.info.questao.id
            this.questao.tipo = this.info.questao.tipo
            this.questao.comando = this.info.questao.comando
            this.questao.opcoes = this.info.questao.opcoes
            this.questao.valor = this.info.questao.valor
            this.questao.gabarito = this.info.questao.gabarito
          } else {
            throw new Error(response.data.message)
          }
        })
        .catch((err) => {
          alert(err);
        });}
    event.preventDefault();

    return {questao, update}
  },

  methods: {
    addOpcao(opcao, event){
      this.questao.opcoes.push(opcao)
      event.preventDefault();
    },
    removeOpcao(opcao,event){
      var i = this.questao.opcoes.indexOf(opcao)
      this.questao.opcoes.splice(i,1)
      event.preventDefault();
    },
    save(event){
      const path = `${import.meta.env.VITE_API_URL}/prova/${this.$route.params.id}/questao/${this.$route.params.questao_id}/${this.$route.params.method}`;
      axios.post(path, this.questao, {
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){
          this.$router.push(`/prova/${this.$route.params.id}`)
        } else {
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
    <Navbar />
    <div class="hero-body">
        <div class="column is-4 is-offset-4">
          <h3 v-if="update" class="title">Update Questao</h3>
          <h3 v-else class="title">Create Questao</h3>

          <div class="questao">

            <input type="text" v-model="questao.comando">

            <select v-model="questao.tipo">
              <option value="vf">Verdadeiro/Falso</option>
              <option value="mul">Multipla Escolha</option>
              <option value="num">Valor Numerio</option>
            </select>
            
            <div class="valor">
              Valor: <input type="number" v-model="questao.valor">
            </div>

            <ul class="opcoes">
              <li v-for="o in questao.opcoes" class="questao" v-bind:key="o">
                {{o}} - <button v-on:click="removeOpcao(o)">Delete</button>
              </li>
              <li class="questao">
                Adicionar questao: <input type="text" v-model="opcao" v-on:click="addOpcao(opcao)">
              </li>
            </ul>
            
            <div class="gabarito">
              <div v-if="questao.tipo === 'mul' || questao.tipo === 'vf'" class="mul">
                Gabarito:
                <select v-model="questao.gabarito">
                  <option v-for="o in questao.opcoes" v-bind:key="o">{{o}}</option>
                </select>
              </div>
              <div class="num">
                Gabarito: <input type="number" v-model="questao.gabarito">
              </div>
            </div>
          </div>

          <div class="button" id="SalvarQuestao">
            <button v-on:click="save">Salvar Questao</button>
          </div>
        </div>
    </div>
</template>
