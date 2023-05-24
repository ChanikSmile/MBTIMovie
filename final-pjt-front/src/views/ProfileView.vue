<template>
  <div class="row py-5 px-4">
    <div class="col-sm-8">
      <div class="col">
        <div class="bg-white_shadow_rounded_overflow-hidden">
          <div class="d-flex">
            <div class="name" style="height:250px; width:250px ">
              <div class="media align-items-end profile-head">
                <div class="about">
                  <div class="profile" style="text-align:center">
                    <img src="@/assets/arsenal.png" alt="..." width="180" class="rounded">
                  </div>
                </div>
              </div>
              </div>
              <div style="margin-left: 30px; margin-top: 20px;">
                <div class="d-flex" style="margin-bottom: 35px;">
                  <div style="font-size:23px; font-weight:bold; margin-right: 50px; margin-top: 15px;">😃 {{ user_info[0].username }}</div>
                  <div class="d-flex">
                    <div>
                      <div style="text-align:center; font-weight:bold;">{{ user_like_movies.length}}</div>
                      <div style="margin-top:5px; margin-right:20px">❤️좋아요를 누른 영화</div>
                    </div>
                  </div>
                </div>
              <div>
                <div style="margin-top: 10px; text-align: left;">⚽ MBTI : {{ user_info[0].mbtis }}</div>
              </div>
            </div>
          </div>
          <div class="py-4 px-4">
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 style="font-weight:bold; margin-left:10px">❤️좋아요를 누른 영화</h5>           
          </div>
          <div class="p-4 rounded shadow-sm bg-light">
            <div class="row">
              <div v-if="user_like_movies" class="container-fluid">
                  <ProfileMovie v-for="movie in user_like_movies"
                  :key="movie.id"
                  :movie="movie"></ProfileMovie>
              </div>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between mb-3">
            <h5 style="font-weight:bold; margin-left:10px">❤️좋아요를 누른 영화로 추천</h5>           
          </div>
          <div class="p-4 rounded shadow-sm bg-light">
            <div class="row">
              <div v-if="user_like_recommends" class="container-fluid">
                  <ProfileRecommendMovie v-for="movie in user_like_recommends[0]"
                  :key="movie.id"
                  :movie="movie['fields']"></ProfileRecommendMovie>
              </div>
            </div>
          </div>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>
  
<script>

import { mapState } from 'vuex'
import ProfileMovie from './ProfileMovie.vue'
import ProfileRecommendMovie from './ProfileRecommendMovie.vue'

  
  export default {
    name: "ProfileView",
    components: {
      ProfileMovie,
      ProfileRecommendMovie
    },
    data() {
      return {
        // userId: this.$route.params.userId,
        // keyvalue: 'like_movies',
        // slide: 0,
        // sliding: null,
      }
    },
  
    computed: {
      ...mapState(['user_info', 'user_like_movies', 'user_like_recommends']),
      isLogin() {
      return this.$store.getters.isLogin;
      },
      
    },
  
    methods: {
    },
  
    created() {
      this.$store.dispatch('userLikeMovies')
      this.$store.dispatch('userLikeRecommends')
    },
  }
</script>
  
<style scoped>
  .my-block {
    background-color: black;
  }
  
  .profile-head {
      transform: translateY(3rem)
  }
  
  
  .is-circle {
    background-color:darkgray;
  }
  
  
  .name{
    animation: hue-rotate 2s linear infinite alternate;
    color: rgb(26, 26, 26);
    border-radius: 5px;
    display: inline-block;
  
  }
  
  /* @keyframes hue-rotate {
    to{ filter: hue-rotate(90deg)}
  }
   */
  
    .update:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: #BC41AB 0px 0px 0px;
    }
  
    .movie_update{
      background-color: #E92964;
      box-shadow: #BC41AB 4px 4px 0px;
      border-radius: 5px;
      transition: transform 200ms, box-shadow 200ms;
      color : #fff;
      width: 175px;
      height: 40px;
      text-align: center;
      outline: none;
    

    }
  
    .movie_update:active{
      transform: translateY(4px) translateX(4px);
      box-shadow: #BC41AB 0px 0px 0px;
    }
  
</style>