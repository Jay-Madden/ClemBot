<template>
  <div id="feature-card" class="tile is-parent mx-3 has-text-centered">
    <article class="tile is-child notification is-dark">
      <p class="title">{{ title }}</p>
      <div class="divider">About</div>
      <div class="block">
        <p class="subtitle">
          {{ description }}
        </p>
      </div>

      <div id="nav-child" class="has-shadow">
        <b-image id="help-image" :src="image" />
      </div>
    </article>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      required: true,
    },
  },
}
</script>

<style scoped>
#help-image {
  box-shadow: rgba(0, 0, 0, 0.4) 0px 6px 7px,
    rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
}

.divider {
  color: #ffffff;
}
</style>
