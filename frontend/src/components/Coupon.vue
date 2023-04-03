<template>
  <div class="mb-8  border  border-black">
    <div class="px-4  py-2  bg-orange-500"><!-- Brand banner -->
      <slot name="brand-name"></slot>
    </div>
    <div class="py-5  text-center  text-2xl"><!-- Code section -->
      <slot name="coupon-code"></slot>
    </div>
    <div class="px-4  py-2  bg-orange-500"><!-- Expiry banner -->
      Expires: <slot name="expiry-date"></slot>
    </div>
  </div>
</template>
