<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { ref } from 'vue';
import QuestaoComponent from "../components/Questao";

export default {
  name: "ProvaView",
  components: {QuestaoComponent},
  setup() {
    var info = {}
    const path = `${import.meta.env.VITE_API_URL}/prova/${this.$route.params.id}`;
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

    return {info}
  },

  methods: {
    addQuestao(event){
      this.router.push(`/prova/${this.$route.params.id}/questao/0/create`)
      event.preventDefault();
    }
  },
}
</script>

<template>
    <Navbar />
    <div class="hero-body">
        <div class="column is-4 is-offset-4">
          <h3 class="title">Prova</h3>
          <div class="questoes">
            <div class="questao" v-for="q in info.questoes" :key="q">
              <QuestaoComponent  v-bind="q" :edit="info.edit"/>
            </div>
          </div>
          <div class="button" id="AddQuestao">
            <button v-on:click="addQuestao">Adicionar Questao</button>
          </div>
        </div>
    </div>
</template>
