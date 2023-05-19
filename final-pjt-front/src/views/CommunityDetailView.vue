<template>
    <div>
    <h1>Detail</h1>
    <h3>글제목</h3>
    <p>글 번호 : {{ community?.id }}</p>
    <p>제목 : {{ community?.title }}</p>
    <p>내용 : {{ community?.content }}</p>
    <p>작성시간 : {{ community?.created_at }}</p>
    <p>수정시간 : {{ community?.updated_at }}</p>
    <h5>댓글</h5>
    <div v-for="comment in comments" :key="comment.id">
      <p>내용: {{ comment.content }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: "CommunityDetailView",
  data() {
    return {
      community : null,
      comments: null
    }
  },
  created() {
    this.getCommunityDetail()
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${ this.$route.params.id }/`
      })
      .then((res) => {
        this.community = res.data.community
        this.comments = res.data.comments
        console.log(this.comments)
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>