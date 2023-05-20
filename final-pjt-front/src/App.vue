<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark">
      <img
        src="./assets/Persona.png"
        alt="로고 이미지"
        style="width: 180px; height: 180px"
      />
      <b-nav-item> <router-link to="/">Home</router-link> | </b-nav-item>
      <b-nav-item> <router-link to="/movie">Movie</router-link> | </b-nav-item>
      <b-nav-item>
        <router-link :to="{ name: 'login' }">로그인</router-link> |
      </b-nav-item>
      <b-nav-item>
        <router-link :to="{ name: 'community' }">커뮤니티</router-link> |
      </b-nav-item>
      <b-nav-item>
        <router-link to="/signup">회원가입</router-link>
      </b-nav-item>
    </b-navbar>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: black;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
