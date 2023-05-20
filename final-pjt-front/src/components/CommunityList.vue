<template>
  <div class="community-list">
    <h3>Community List</h3>
    <CommunityListItem 
    v-for="community in communitys" :key="community.id" :community="community"
    />
  </div>
</template>

<script>
import CommunityListItem from '@/components/CommunityListItem'

export default {
  name: 'CommunityList',
  components: {
    CommunityListItem,
  },
  computed: {
    communitys() {
      return this.$store.state.communitys
    }
  }
}
</script>

<style>
.community-list {
  text-align: start;
}
</style>
