<template>
  <div>
    <b-navbar class="is-transparent has-background-primary shadow fixed-top">
      <template #brand>
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          Clembot Logo</b-navbar-item
        >
      </template>
      <template #start>
        <b-navbar-item
          id="nav"
          class="is-spaced is-tab"
          tag="nuxt-link"
          :to="{ path: '/wiki' }"
        >
          Wiki
        </b-navbar-item>
        <b-navbar-item
          class="is-spaced is-tab"
          tag="nuxt-link"
          :to="{ path: '/about' }"
        >
          About
        </b-navbar-item>
      </template>

      <template #end>
        <b-navbar-item
          class="is-spaced"
          tag="nuxt-link"
          :to="{ path: '/about' }"
        >
          <div id="login" class="box has-background-primary">
            <div class="columns">
              <div class="column has-text-centered has-text-white">
                <b> Login With Discord </b>
              </div>
              <div class="animation-wrapper">
                <discord-logo class="mr-4 mt-1" />
              </div>
            </div>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>

    <section class="main-content">
      <div class="container column">
        <nuxt />
      </div>
    </section>
  </div>
</template>
<style scoped>
#login :hover + .animation-wrapper {
  animation-name: ckw;
  animation-duration: 1.5s;
  /* Things added */
  animation-iteration-count: infinite;
  transform-origin: 30% 45%;
  display: inline-block;
  /* <--- */
}
@keyframes ckw {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
