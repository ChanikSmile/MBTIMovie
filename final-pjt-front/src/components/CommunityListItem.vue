<template>
  <div>
    <h5>{{ community.id }}</h5>
    <p>{{ community.title }}</p>
    <router-link :to="{
      name: 'CommunityDetailView',
      params: {id: community.id }}">
      [DETAIL]
    </router-link>
    <br>
    <button @click="likeCommunity(community.id)">Like</button>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    community: Object,
  },
  methods: {
    likeCommunity(communityId) {
      const payload = {communitys: this.$store.state.communitys, communityId: communityId}
      this.$store.dispatch('likeCommunity', payload)
      
    }
  }
}
</script>

<style>

</style>
