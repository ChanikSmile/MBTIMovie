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
    <p>작성자: {{ comment.user.username }}</p>
  </div>

  <form @submit.prevent="createComment">
  <label for="comment-content">댓글 작성:</label>
  <input type="text" id="comment-content" v-model="newCommentContent">
  <button type="submit">등록</button>
</form>

</div>

</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
name: "CommunityDetailView",
data() {
  return {
    community : null,
    comments: null,
    newCommentContent: null,
  }
},
created() {
  this.getCommunityDetail()
},
computed: {
  ...mapState(['token']),
  ...mapState(['user_info'])
},
methods: {
  getCommunityDetail() {
    const token = this.token
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/${ this.$route.params.id }/`,
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then((res) => {
      this.community = res.data.community
      this.comments = res.data.comments

    })
    .catch(err => {
      console.log(err)
    })
  },
  createComment() {
    const token = this.token;
    const commentContent = this.newCommentContent;
    const communityId = this.community.id;
    const user_id = this.user_info[0].user_id

    console.log(user_id)
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/community/${communityId}/`,
      data: { content: commentContent, user:user_id},
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        const newComment = res.data;
        this.comments.push(newComment);
        this.newCommentContent = ''; // 댓글 작성 폼 초기화
        console.log('댓글이 성공적으로 생성되었습니다:', newComment);
      })
      .catch((err) => {
        console.log('댓글 생성에 실패했습니다:', err);
      });
  },
},
}
</script>

<style>
</style>
