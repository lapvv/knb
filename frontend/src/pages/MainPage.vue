<template>
  <div>MainPage</div>
  <div>Enter your name:</div>
  <input v-model="name" type="text" />
  <button @click="sendName(name)">Войти</button>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      name: "",
    };
  },
  methods: {
    async sendName(name) {
      await axios
        .post("http://127.0.0.1:8002/", { name: name })
        .then((response) => console.log(response))
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped></style>
