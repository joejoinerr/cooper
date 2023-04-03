<script setup>
import AppHeader from './components/AppHeader.vue'
import CouponList from './components/CouponList.vue'
</script>

<template>
  <AppHeader/>
  <Suspense>
    <CouponList/>
  </Suspense>
</template>

<style scoped>

</style>
