<template>
  <div>
    <div v-for="movie in movies" :key="movie.id">
      <p>{{ movie.title }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/v1";
export default {
  data() {
    return {
      movies: {},
    };
  },
  created() {
    this.getMovies();
  },
  methods: {
    getMovies() {
      axios({
        method: "get",
        url: `${API_URL}/moviegenre`,
      }).then((res) => {
        console.log(res.data);
        this.movies = res.data;
      });
    },
  },
};
</script>

<style></style>
