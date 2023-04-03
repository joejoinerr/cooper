<script setup>
import { ref } from 'vue';
import Coupon from './Coupon.vue';

async function fetchAllCoupons() {
  const res = await fetch('/api/coupons');
  const jsonData = await res.json();
  return jsonData.coupons;
}

const couponList = ref([]);
fetchAllCoupons().then((data) => {
  couponList.value = data
})
</script>

<template>
  <div class="px-4">
    <template v-if="couponList.length">
      <Coupon v-for="coupon in couponList">
        <template #brand-name>
          {{ coupon.brand }}
        </template>
        <template #coupon-code>
          {{ coupon.code }}
        </template>
        <template #expiry-date>
          {{ coupon.expiry }}
        </template>
      </Coupon>
    </template>
    <div v-else class="text-center">
      No coupons yet :)<br>
      Tap "Add" to create one.
    </div>
  </div>
</template>
