<template>
  <svg
    :width="size"
    :height="size"
    class="icon"
    viewBox="0 0 1280 1024"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
        d="M595.7 511.1L240.8 866l93.2 93.1 447.4-447.4-0.6-0.6 0.6-0.5L334 63.1l-93.2 93.2z"
        :fill="fill"
    />
  </svg>
</template>

<script>
export default {
  props: {
    size: {
      type: [Number, String],
      default: 64
    },
    fill: {
      type: String,
      default: "#202020"
    }
  }
}
</script>