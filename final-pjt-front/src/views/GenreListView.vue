<template>
  <div>
    <h1>장르들 보여주기~</h1>
    <div v-if="condition">
      <GenreAll />
    </div>
      <GenreItem />
  </div>
</template>

<script>
import GenreItem from "@/components/GenreItem.vue";
import GenreAll from "@/components/GenreAll.vue";

export default {
  components: {
    GenreItem,
    GenreAll,
  },
  data() {
    return {
      condition: true,
    };
  },
};
</script>

<style></style>
