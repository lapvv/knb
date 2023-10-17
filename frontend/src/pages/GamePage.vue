<template>
  <div>GamePage</div>
  <div>Выберите действие:</div>
  <button @click="sendAction('k')">Камень</button>
  <button @click="sendAction('n')">Ножницы</button>
  <button @click="sendAction('b')">Бумага</button>
</template>

<script>
import axios from "axios";
/* eslint-disable */
export default {
  mounted() {},
  methods: {
    sendAction(action) {
      axios
        .post("127.0.0.1: 8002", { data: action })
        .then((response) => console.log(response));
    },
  },
};
</script>

<style lang="scss" scoped></style>
