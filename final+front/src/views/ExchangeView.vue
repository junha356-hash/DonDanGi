<template>
  <section class="pt-4 pb-2 text-center bg-light border-bottom mb-5">
    <img src="@/assets/exchange.jpg" alt="exchange_img"
    data-aos="fade-out" data-aos-duration="600">
    <h1 class="display-5 fw-bold" data-aos="fade-down" data-aos-duration="1500">환율 계산기</h1>
  </section>
  <div class="container-content px-5">
    <h2 class="fw-bold mb-3">💲 환율 계산</h2>
    <hr>
    <ExchangeComponent />
  </div>
</template>

<script setup>
import ExchangeComponent from '@/components/ExchangeComponent.vue'

</script>

<style scoped>

</style>