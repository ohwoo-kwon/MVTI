<template>
<div>
  <p>{{movie.title}}</p>
  <p>{{movie.overview}}</p>
</div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: Object,
  },
}
</script>

<style>
  #movie-detail {
    height: 100%;
    max-width: 800px;
  }
</style>