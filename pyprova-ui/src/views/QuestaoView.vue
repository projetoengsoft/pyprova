<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { ref } from 'vue';
import jwtDecoder from "../utils/jwtDecoder";

export default {
  name: "QuestaoView",
  setup() {
    var update = false
    const renderComponent = ref(true);
    var isLogged = ref(sessionStorage.getItem('token'))
    var opcao = null
    var vf = ['Verdadeiro', 'Falso']

    var questao = ref({'id': null,
                   'tipo': null,
                   'comando': null,
                   'opcoes': [],
                   'valor': 1,
                   'gabarito': null})

    return {isLogged, questao, update, renderComponent, opcao, vf}
  },

  mounted() {
    if(this.$route.params.method === 'update'){
      this.update = true
    }
    if (!this.isLogged) {
      alert('You are not logged!')
      this.$router.push('login')
    } else {
      console.log(jwtDecoder(this.isLogged, 'sub'));
    }
    if (this.update) {
      this.get()
    }
  },

  methods: {
    async get() {
      const path = `${import.meta.env.VITE_API_URL}prova/${this.$route.params.id}/questao/${this.$route.params.questao_id}/detail`;
      var request = {
      headers: {
        'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
      }
    }
    this.questao = await axios.get(path,request)
        .then(response => {
          if (response.data.success) {
            this.forceRender()
            return response.data.message.questao
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
    addOpcao(event){
      this.questao.opcoes.push(this.opcao)
      this.opcao = null
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
  }
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <div class="column is-4 is-offset-4">
          <h3 v-if="update" class="title">Update Questao</h3>
          <h3 v-else class="title">Create Questao</h3>

          <div class="questao">
            <div>
              <label>Tipo:</label>
              <select v-model="questao.tipo" v-on:change="forceRender">
              <option value="vf">Verdadeiro/Falso</option>
              <option value="mul">Multipla Escolha</option>
              <option value="num">Valor Numerio</option>
            </select>
            </div>

            <div>
              <label>Comando:</label>
              <input type="text" v-model="questao.comando">
            </div>


            <div class="valor">
              Valor: <input type="number" v-model="questao.valor">
            </div>

            <ul v-if="questao.tipo === 'mul'" class="opcoes">
              <li v-for="o in questao.opcoes" class="questao" v-bind:key="o">
                {{o}} - <button v-on:click="removeOpcao(o)">Delete</button>
              </li>
              <li class="questao">
                Adicionar questao: <input type="text" v-model="opcao" >
                <button v-on:click="addOpcao()">+</button>
              </li>
            </ul>

            <div class="gabarito">
              <div v-if="questao.tipo === 'mul'" class="mul">
                Gabarito:
                <select v-model="questao.gabarito">
                  <option v-for="o in questao.opcoes" v-bind:key="o">{{o}}</option>
                </select>
              </div>
              <div v-if="questao.tipo === 'vf'" class="mul">
                Gabarito:
                <select v-model="questao.gabarito">
                  <option v-for="o in vf" v-bind:key="o">{{o}}</option>
                </select>
              </div>
              <div v-if="questao.tipo === 'num'" class="num">
                Gabarito: <input type="number" v-model="questao.gabarito">
              </div>
            </div>
          </div>

          <div id="SalvarQuestao">
            <button v-on:click="save">Salvar Questao</button>
          </div>
        </div>
    </div>
</template>