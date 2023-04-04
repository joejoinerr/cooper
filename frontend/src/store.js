import { reactive } from 'vue'

export const couponList = reactive({
  items: [],
  refreshCouponList() {
    return fetch('/api/coupons')
      .then((res) => res.json())
      .then((jsonData) => this.items = jsonData.coupons)
  }
})
