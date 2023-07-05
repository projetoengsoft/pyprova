<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';
import { ref } from 'vue';

export default{
  setup() {
    var inputFields = ref({
      email: '',
      password: '',
    })

    return {
      inputFields
    }
  },
  methods: {
    getFields(event){
      const path = `${import.meta.env.VITE_API_URL}login`;
      axios.post(path, this.inputFields, {
        headers:{
          'Content-Type': 'application/json'
        }
      })
      .then((res) => {
        if(res.data.success){
          sessionStorage.setItem('token', 'jwt-token')
          console.log('redirect to profile')
        } else {
          throw new Error(res.data.message)
        }
      })
      .catch((err) => {
        console.log(err);
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
            <h3 class="title">Login</h3>
            <div class="box">
                <form>
                    <div class="field">
                        <div class="control">
                          <input class="input is-large" type="email" 
                          placeholder="Your Email" autofocus="" v-model="inputFields.email">
                        </div>
                    </div>
    
                    <div class="field">
                        <div class="control">
                            <input class="input is-large" type="password"
                            placeholder="Your Password" v-model="inputFields.password">
                        </div>
                    </div>
                    <!-- <div class="field">
                        <label class="checkbox">
                            <input type="checkbox" name="remember">
                            Remember me
                        </label>
                    </div> -->
                    <button v-on:click="getFields" 
                    class="button is-block is-info is-large is-fullwidth">
                      Login
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>
