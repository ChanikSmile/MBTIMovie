import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";
import router from "../router";

import createPersistedState from "vuex-persistedstate";

const API_URL = "http://127.0.0.1:8000";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: null,
  },
  getters: {},
  mutations: {
    // SIGN_UP(state, token){
    //   state.token = token
    // },
    SAVE_TOKEN(state, token) {
      if (router.currentRoute.path !== "/") {
        state.token = token;
        console.log(state.token);
        router.push({ name: "home" });
      }
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const name = payload.name;
      const mbtis = payload.mbtis;
      const genders = payload.genders;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          name,
          mbtis,
          genders,
        },
      })
        .then((res) => {
          console.log(res.data);
          //context.commit('SIGN_UP', res.data.key)
          context.commit("SAVE_TOKEN", res.data.key);
          console.log("잘들어갔음!");
        })
        .catch((err) => {
          console.log(err);
        });
    },

    login(context, payload) {
      const username = payload.username;
      const password = payload.password;
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key);
          console.log("로그인 성공!");
        })
        .catch((err) => {
          console.log(err);
          console.log("실패...");
        });
    },
  },
  modules: {},
});
