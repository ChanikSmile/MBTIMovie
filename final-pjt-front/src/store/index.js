import Vue from "vue";
import Vuex from "vuex";

import axios from "axios";
import router from "../router";

import createPersistedState from "vuex-persistedstate";

const HOME_URL = "http://127.0.0.1:8000";

const API_URL = "https://api.themoviedb.org/3/movie/now_playing?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR";
const POPULAR_URL = "https://api.themoviedb.org/3/movie/popular?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR"


Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    newMovieList: [],
    popularMovieList: [],
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
    GET_MOVIES(state, newMovieList) {
      state.newMovieList = newMovieList
    },
    GET_POPULAR_MOVIES(state, popularMovieList) {
      state.popularMovieList = popularMovieList
    },
  },
  actions: {
    // 최신영화 가져오기!
    getMovies(context) {
      axios({
        method: "get",
        language: "ko-KR",
        url: API_URL,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data.results)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    // 인기영화 가져오기!
    getPopularMovies(context) {
      axios({
        method: "get",
        url: POPULAR_URL,
      })
        .then((res) => {
          context.commit('GET_POPULAR_MOVIES', res.data.results)
        })
        .catch((err) => {
          console.log(err);
        });
    },

    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const name = payload.name;
      const mbtis = payload.mbtis;
      const genders = payload.genders;

      axios({
        method: "post",
        url: `${HOME_URL}/accounts/signup/`,
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
        url: `${HOME_URL}/accounts/login/`,
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
