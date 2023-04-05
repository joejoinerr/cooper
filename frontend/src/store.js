import { reactive } from 'vue'

export const couponList = reactive({
  items: [],
  refresh() {
    return fetch('/api/coupons')
      .then((res) => res.json())
      .then((jsonData) => this.items = jsonData.coupons)
  }
})
