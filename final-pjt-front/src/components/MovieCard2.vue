<template>
  <div>
    <h1>인기영화</h1>
    <div id="carouselPopularPlaying" class="carousel slide" data-bs-ride="carousel">
      <ol class="carousel-indicators">
        <li
          data-bs-target="#carouselPopularPlaying"
          v-for="(group, index) in groupMovies2"
          :key="index"
          :data-bs-slide-to="index"
          :class="{ active: index === 0 }"
        ></li>
      </ol>
      <div class="carousel-inner">
        <div
          class="carousel-item"
          v-for="(group, index) in groupMovies2"
          :key="index"
          :class="{ active: index === 0 }"
        >
          <div class="row">
            <div class="col-3" v-for="movie in group" :key="movie.id">
              <img
                :src="getImageUrl(movie.poster_path)"
                class="d-block w-100"
                :alt="movie.title"
                style="height: 40rem"
              />
            </div>
          </div>
        </div>
      </div>
      <a
        class="carousel-control-prev"
        href="#carouselPopularPlaying"
        role="button"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </a>
      <a
        class="carousel-control-next"
        href="#carouselPopularPlaying"
        role="button"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard2",
  methods: {
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
  },
  computed: {
    popularMovieList() {
      return this.$store.state.popularMovieList;
    },
    groupMovies2() {
      const movieSize = 4;
      const sizes = [];
      for (
        let i = 0;
        i < this.$store.state.popularMovieList.length;
        i += movieSize
      ) {
        sizes.push(this.$store.state.popularMovieList.slice(i, i + movieSize));
      }
      return sizes;
    },
  },
};
</script>

<style></style>
