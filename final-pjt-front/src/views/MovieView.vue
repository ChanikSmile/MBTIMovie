<template>
  <div class="justify-content-center">
    <MovieCard1 />
    <hr>
    <MovieCard2 />
  </div>
</template>

<script>
import MovieCard1 from '@/components/MovieCard1.vue'
import MovieCard2 from '@/components/MovieCard2.vue'

export default {
  name: 'MovieView',
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    getPopularMovies() {
      this.$store.dispatch('getPopularMovies')
    }
  },
  components: {
    MovieCard1,
    MovieCard2
  },
  created() {
    this.getMovies();
    this.getPopularMovies();
  },
  computed: {
    newMovieList() {
      return this.$store.state.newMovieList
    },
    popularMovieList() {
      return this.$store.state.popularMovieList
    }
  }
}
</script>


<style>

</style>
