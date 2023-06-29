<script setup>
import Navbar from '../components/Navbar.vue';
</script>

<script>
import axios from 'axios';
// export default {
//   name: 'Ping',
//   data() {
//     return {
//       msg: '',
//     };
//   },
//   methods: {
//     getMessage() {
//       const path = `${import.meta.env.VITE_API_URL}ping`;
//       axios.get(path)
//         .then((res) => {
//           this.msg = res.data;
//         })
//         .catch((error) => {
//           console.error(error);
//         });
//     },
//   },
//   created() {
//     this.getMessage();
//   },
// };
</script>

<template>
  <Navbar />
  <div class="hero-body">
    <div class="container has-text-centered">
      <h1 class="title">
        Flask Login Example
      </h1>
      <h2 class="subtitle">
        Easy authentication and authorization in Flask.
      </h2>
      </div>
  </div>
</template>
