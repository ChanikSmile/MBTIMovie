<template>
  <div>
    <h5>{{ community.id }}</h5>
    <p>{{ community.title }}</p>
    <router-link :to="{
      name: 'CommunityDetailView',
      params: {id: community.id }}">
      [DETAIL]
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'CommunityListItem',
  props: {
    community: Object,
  }
}
</script>

<style>

</style>
