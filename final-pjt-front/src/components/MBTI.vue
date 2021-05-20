<template>
  <li @click="showMbti">
    {{ mbti }}
  </li>
</template>

<script>
export default {
  name: 'MBTI',
  props: {
    mbti: String,
  },
  methods: {
    showMbti: function () {
      // console.log(this.mbti)
      this.$emit('show-mbti', this.mbti)
    }
  }
}
</script>

<style scoped>
  li {
    cursor: pointer;
  }
</style>