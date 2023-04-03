<script setup>
  defineProps(['buttonClass'])
</script>

<template>
  <button class="block  px-4  py-3  leading-4" :class="buttonClass">
    <slot></slot>
  </button>
</template>
