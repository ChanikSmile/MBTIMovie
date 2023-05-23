<template>
  <div>
    <h1>로그인 창입니다.</h1>
    <form @submit.prevent="login">
      <label for="username">ID : </label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password">password : </label>
      <input type="password" id="password" v-model="password">
      <br>

      <input type="submit" value="로그인" @click="login">
    </form>
  </div>
</template>

<script>

export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login',payload)
    },
  logout() {
    this.$store.dispatch('logout')
  }
  }
}
</script>

<style>
</style>
