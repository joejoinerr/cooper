<script setup>
import { format } from 'date-fns';
import { ref } from 'vue';
import { couponList } from './store.js'
import AppHeader from './components/AppHeader.vue';
import Coupon from './components/Coupon.vue';

couponList.refresh()

function isoDate(date) {
  return format(new Date(date), 'yyyy-MM-dd')
}
</script>

<template>
  <AppHeader/>
  <div class="px-4">
    <template v-if="couponList.items.length">
      <Coupon class="mb-8" v-for="coupon in couponList.items">
        <template #brand-name>
          {{ coupon.brand }}
        </template>
        <template #coupon-code>
          {{ coupon.code }}
        </template>
        <template #expiry-date>
          {{ coupon.expiry ? isoDate(coupon.expiry) : 'never' }}
        </template>
      </Coupon>
    </template>
    <div v-else class="text-center">
      No coupons yet :)<br>
      Tap "Add" to create one.
    </div>
  </div>
</template>
