<script>
import Navbar from '../components/Navbar.vue'
import profileTypes from '../utils/profileTypes';
import axios from 'axios';
import { ref } from 'vue';

export default{
  setup() {
    var inputFields = ref({
      email: '',
      name: '',
      password: '',
      profile: 0,
    })

    var isLogged = ref(sessionStorage.getItem('token'))

    return {
      inputFields,
      isLogged,
      profileTypes,
    }
  },
  methods: {
    getFields(event){
      if(this.inputFields['profile'] === 0){
        alert('You must choose a profile!');
      } else {
        const path = `${import.meta.env.VITE_API_URL}signup`;
        axios.post(path, this.inputFields, {
          headers:{
            'Content-Type': 'application/json'
          }
        })
        .then((res) => {
          if(res.data.success){
            alert(res.data.message)
            this.$router.push('login')
          } else {
            throw new Error(res.data.message)
          }
        })
        .catch((err) => {
          alert(err);
        });
      }
      event.preventDefault();
    }
  },
  mounted() {
    if(this.isLogged) {
      this.$router.push('profile')
    }
  }
}

</script>

<template>
    <Navbar />
    <div class="hero-body">
        <div class="column is-4 is-offset-4">
            <h3 class="title">Sign Up</h3>
            <div class="box">
                <form>
                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="email" 
                          placeholder="Email" autofocus="" v-model="inputFields.email">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="text"
                          placeholder="Name" autofocus="" v-model="inputFields.name"> 
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="password"
                          placeholder="Password" v-model="inputFields.password">
                        </div>
                    </div>

                    <div class="field">
                      <div class="control">
                        <label class="label">Select a profile</label>
                        <div class="select">
                          <select v-model="inputFields.profile">
                            <option v-for="pType in profileTypes" v-bind:value="pType.cod">
                              {{ pType.description }}
                            </option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <button v-on:click="getFields" class="button is-block is-info is-large is-fullwidth">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
</template>