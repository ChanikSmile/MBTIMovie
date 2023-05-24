<template>
  <div>
    <h3>{{ this.movie_genre }} 영화 목록</h3>
    <div class="btn-group">
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(1, '전체')">전체</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(12, '모험')">모험</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(14, '판타지')">판타지</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(16, '애니메이션')"
          >애니메이션</a
        >
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(18, '드라마')">드라마</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(27, '공포')">공포</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(28, '액션')">액션</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(35, '코미디')">코미디</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(36, '역사')">역사</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(37, '서부')">서부</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(53, '스릴러')">스릴러</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(80, '범죄')">범죄</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(99, '다큐멘터리')"
          >다큐멘터리</a
        >
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(878, 'SF')">SF</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(9648, '미스터리')">미스터리</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10402, '음악')">음악</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10749, '로맨스')">로맨스</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10751, '가족')">가족</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10752, '전쟁')">전쟁</a>
      </button>
      <button type="button" class="btn btn-light">
        <a class="dropdown-item" @click="sortBtn(10770, 'TV 영화')">TV 영화</a>
      </button>
    </div>

    <div v-if="sortBtn">
      <template v-if="genres.length">
        <div class="card-group">
          <div v-for="genre in genres" :key="genre.id">
            <div class="card">
              <router-link
                :to="{ name: 'MovieDetail', params: { id: genre.id } }"
              >
                <img
                  :src="getImageUrl(genre.poster_path)"
                  class="card-img-top"
                  alt="이미지를 표시할 수 없습니다."
                />
              </router-link>
              <div class="card-body">
                <h5 class="card-title">{{ genre.title }}</h5>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <h3>
          해당 영화 정보가 없습니다. 빠른 시일 내에 데이터를 제공해드리겠습니다.
        </h3>
      </template>
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
      genres: {},
      movie_genre: "",
    };
  },
  created() {
    this.recommendMovie(1);
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
    recommendMovie(num) {
      axios({
        method: "get",
        url: `${API_URL}/${num}/sort`,
      }).then((res) => {
        console.log(res.data);
        this.genres = res.data;
      });
    },
    sortBtn(num, movie_genre) {
      this.movie_genre = movie_genre;
      this.recommendMovie(num);
    },
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
  },
};
</script>

<style></style>
