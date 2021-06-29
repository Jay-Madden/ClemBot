<template>
  <div>
    <nuxt-link :to="{ path: '/' }">
      <img
        id="main-logo"
        class="mx-3 mt-3"
        src="ClemBotLogo.svg"
        alt="ClemBot"
        width="7%"
      />
    </nuxt-link>
    <b-navbar
      class="is-transparent has-background-primary has-shadow is-fixed-top mb-4"
    >
      <template #start>
        <b-navbar-item
          id="nav"
          class="is-spaced is-tab"
          tag="nuxt-link"
          :to="{ path: '/wiki' }"
        >
          <b-icon icon="script" class="mr-1" size="is-small" /><b> Wiki </b>
        </b-navbar-item>
        <b-navbar-item
          id="nav"
          class="is-spaced is-tab"
          tag="nuxt-link"
          :to="{ path: '/about' }"
        >
          <b-icon icon="information-outline" class="mr-1" size="is-small" /><b
            >About</b
          >
        </b-navbar-item>
        <b-navbar-item
          id="nav"
          class="is-spaced is-tab"
          tag="nuxt-link"
          :to="{ path: '/status' }"
        >
          <b-icon icon="heart-cog-outline" class="mr-1" size="is-small" />
          <b>Status</b>
        </b-navbar-item>
      </template>
      <template #end>
        <b-navbar-item
          href="https://discord.com/api/oauth2/authorize?client_id=710672266245177365&permissions=1543630070&scope=bot"
        >
          <b-button icon-left="plus" class="is-primary">
            <b>Invite to Server </b>
          </b-button>
        </b-navbar-item>
        <b-navbar-item href="https://discord.gg/mhrVuyh">
          <b-icon id="tray-icons" icon="discord"> </b-icon>
        </b-navbar-item>
        <b-navbar-item
          id="tray-icons"
          href="https://github.com/ClemBotProject/ClemBot"
        >
          <b-icon icon="github"> </b-icon>
        </b-navbar-item>
        <!--
        <b-navbar-item tag="nuxt-link" :to="{ path: '/about' }">
          <b-button id="discord-login" class="has-text-centered is-ghost">
            <div class="columns is-vcentered">
              <div class="column">
                <b> Login </b>
              </div>
              <div class="animation-wrapper">
                <div id="discord-login-logo" class="column">
                  <discord-logo class="mt-2" />
                </div>
              </div>
            </div>
          </b-button>
        </b-navbar-item>
        -->
      </template>
    </b-navbar>
    <section class="main-content">
      <nuxt />
    </section>
  </div>
</template>
<style scoped lang="scss">
.section {
  height: 40%;
}

#main-logo {
  position: fixed;
  z-index: 200;
}

#discord-login {
  background: #5865f2;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
  text-decoration: none;
}

#nav {
  left: 38%;
}

#tray-icons {
  transition: all 1.2s ease-in-out;
}

#tray-icons :hover {
  transform: scale(1.1);
  color: white;
}

#discord-login :hover + .animation-wrapper {
  animation-name: ckw;
  animation-duration: 1.5s;
  /* Things added */
  animation-iteration-count: infinite;
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
