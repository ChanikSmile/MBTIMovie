<template>
  <div>
    <h1>Community Page</h1>
    <router-link :to="{name: 'CommunityCreateView'}">[CREATE]</router-link>
    <CommunityList />
    <hr>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList.vue'

export default {
  name: 'CommunityView',
  components: {
    CommunityList,
  },
  
  computed:{
    isLogin() {
      return this.$store.getters.isLogin // 로그인 여부
    }
  },
  methods: {
    getCommunity() {
      this.$store.dispatch('getCommunity')
    }
  },

  created() {
    this.getCommunity()
  },
  

}
</script>

<style>

</style>