<template>
  <div>
    <div class="movie-detail-card">
      <div class="movie-detail-body">
        <div class="movie-detail-poster">
          <img :src="getImageUrl(movie.poster_path)" :alt="movie.title" />
        </div>
        <div class="movie-detail-info">
          <!-- info header -->
          <div class="movie-detail-upper">
            <div class="movie-detail-info-header">
              <div class="movie-detail-info-header-left">
                <div class="movie-detail-title">
                  {{ movie.title }}
                </div>
                <div v-if="movie.release_date" class="movie-release-date">
                  개봉 : {{ movie.release_date }}
                </div>
              </div>
              <div class="movie-detail-info-header-right">
                <div class="movie-vote">
                  {{ movie.vote_average }}
                </div>
                <img id="movie-star" src="@/assets/star.png" />
              </div>
            </div>
            <div class="movie-detail-overview-header">줄거리</div>
            <hr />
            <div v-if="movie.overview" class="movie-detail-overview-body">
              {{ movie.overview }}
            </div>
            <div v-else class="movie-detail-overview-body">
              해당 영화는 줄거리가 제공되지 않습니다.
            </div>
          </div>
          <div class="movie-detail-lower">
            <div class="movie-youtube-area">
              관련 영상
              <hr />
              <button
                v-b-modal.modal-xl
                class="btn btn-outline-light"
                @click="getVideo()"
              >
                영상 보러가기!
              </button>
            </div>
          </div>
          <div class="movie-detail-lower">
            <div class="movie-youtube-area">
              이 영화를 한 문장으로 표현한다면?
              <hr />
              
            </div>
          </div>
        </div>
      </div>
    </div>
    <b-modal
      id="modal-xl"
      size="xl"
      header-bg-variant="dark"
      header-text-variant="light"
      body-bg-variant="dark"
      body-text-variant="light"
      footer-bg-variant="dark"
      footer-text-variant="light"
    >
      <iframe
        width="100%"
        height="500"
        :src="movieVideo"
        frameborder="0"
      ></iframe>
      <template #modal-footer="{ cancel }">
        <b-button size="sm" variant="outline-secondary" @click="cancel()">
          닫기
        </b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "https://api.themoviedb.org/3/movie";

export default {
  name: "MovieDetail",
  created() {
    this.getMovieDetail();
  },
  data() {
    return {
      movie: "",
      movieVideo: "",
    };
  },
  methods: {
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/${this.$route.params.id}?api_key=a51700c7b5c0eac2db0ce7a959dcc750&language=ko-KR`,
      })
        .then((res) => {
          console.log(res);
          this.movie = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getImageUrl(posterPath) {
      if (posterPath) {
        return "https://image.tmdb.org/t/p/w220_and_h330_face/" + posterPath;
      }
    },
    getVideo() {
      const videoUrl = `https://api.themoviedb.org/3/movie/${this.$route.params.id}/videos?api_key=a51700c7b5c0eac2db0ce7a959dcc750`;

      axios({
        method: "get",
        url: videoUrl,
      })
        .then((res) => {
          // console.log(res.data.results)
          const videoKey = res.data.results[0].key;
          this.movieVideo = "https://www.youtube.com/embed/" + videoKey;
          //console.log(this.movieVideo);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.movie-detail-card {
  font-family: "Noto Sans KR", sans-serif;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  padding: 2rem;
  min-height: 100%;
  height: auto;
  background-color: #000000;
  color: white;
}

.movie-detail-toolbar {
  height: 56px;
}

.movie-detail-body {
  display: flex;
  flex-flow: row wrap;
  margin: 1rem;
}

.movie-detail-info {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  margin: 1rem 0 0 4rem;
  width: 60%;
}

.movie-detail-info-header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  height: 80px;
}
.movie-detail-poster > img {
  width: 500px;
}

.movie-detail-title {
  font-size: 40px;
}

.movie-detail-info-header-right {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.movie-vote {
  font-size: 30px;
}

#movie-star {
  height: 50%;
  margin-left: 1rem;
}

.movie-detail-overview-header {
  margin-top: 5rem;
  font-size: 32px;
}

.movie-detail-overview-body {
  font-size: 20px;
}

.movie-youtube-area {
  font-size: 32px;
}
</style>
