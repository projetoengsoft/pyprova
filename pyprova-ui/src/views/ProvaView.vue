<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { ref } from 'vue';
import QuestaoComponent from "../components/Questao.vue";
import jwtDecoder from "../utils/jwtDecoder";

export default {
  name: "ProvaView",
  components: {QuestaoComponent},
  setup() {
    var info = {data:{}}
    const renderComponent = ref(true);
    var isLogged = ref(sessionStorage.getItem('token'))

    return {isLogged, info, renderComponent}
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
      const path = `${import.meta.env.VITE_API_URL}prova/${this.$route.params.id}`;
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
      this.info.data.provas = []
   // Remove MyComponent from the DOM
   this.renderComponent = false;

   // Then, wait for the change to get flushed to the DOM
      await this.$nextTick();

      // Add MyComponent back in
      this.renderComponent = true;
    },
    addQuestao(event){
      this.$router.push({name: 'questaoView', params: {id: this.$route.params.id, questao_id: 0, method: 'create'}})
      event.preventDefault();
    }
  },
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <div v-if="renderComponent" class="column is-4 is-offset-4">
          <h3 class="title">Prova</h3>
          <div class="questoes">
            <div class="questao" v-for="q in info.data.questoes" :key="q">
              <QuestaoComponent  v-bind="q" :edit="info.data.edit"/>
            </div>
          </div>
          <div v-if="info.data.edit" id="AddQuestao">
            <button v-on:click="addQuestao">Adicionar Questao</button>
          </div>
        </div>
    </div>
</template>
