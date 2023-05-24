<template>
  <div id="app">
    <img
      src="./assets/Persona.png"
      alt="로고 이미지"
      style="width: 180px; height: 180px"
    />
    <router-link style="text-decoration: none; color: inherit" to="/movie"
      >Movie</router-link
    >
    |
    <router-link style="text-decoration: none; color: inherit" to="/community"
      >커뮤니티</router-link
    >
    |
    <router-link v-if="!isLogin" style="text-decoration: none; color: inherit" to="/login"
      >로그인 | </router-link
    >
    <router-link v-if="isLogin" style="text-decoration: none; color: inherit" to="/profile"
      >프로필 | </router-link
    >
    
    <a href="#" v-if="isLogin" @click="logout">로그아웃 | </a> 

    <router-link style="text-decoration: none; color: inherit" to="/signup"
      >회원가입</router-link
    >

    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      alert('로그아웃되었습니다.')
      this.$router.push({ name: 'home'})
    }
  }
}
</script>


<style>
* {
  background-color: black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

nav {
  padding: 30px;
  background-color: black;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: rgb(211, 47, 39);
}
</style>
