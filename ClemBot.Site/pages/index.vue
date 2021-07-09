<template>
  <div>
    <section id="splash-image" class="hero has-shadow is-fullheight">
      <div class="hero-body columns is-vcentered">
        <div class="column is-two-fifths">
          <img
            id="main-logo"
            class="mx-6 mt-6 is-justify-content-center is-align-content-center"
            src="ClemBotLogo.svg"
            alt="ClemBot"
          />
        </div>
        <div
          id="splash-card"
          class="card column has-background-black-ter mt-6 mr-6"
        >
          <div class="card-content">
            <h1 class="is-size-1 title has-text-white">ClemBot</h1>
            <p class="subtitle has-text-white">
              The modular and configurable open source Discord Bot for all your
              needs
            </p>
          </div>
          <div class="tile is-ancestor">
            <div class="tile is-vertical is-6">
              <div id="nav-tile" class="tile is-parent">
                <a
                  href="https://discord.com/api/oauth2/authorize?client_id=710672266245177365&permissions=1543630070&scope=bot"
                >
                  <article
                    id="nav-child"
                    class="
                      add-to-discord
                      tile
                      is-child
                      notification
                      is-primary
                      column
                    "
                  >
                    <div class="columns">
                      <p class="title column has-text-centered mt-3">
                        Summon me to your Server!
                      </p>
                      <b-icon
                        class="column is-one-quarter mt-3"
                        icon="discord"
                        custom-size="mdi-48px"
                      />
                    </div>
                  </article>
                </a>
              </div>
              <div id="nav-tile" class="tile is-parent has-shadow">
                <article
                  id="nav-child"
                  class="
                    tile
                    is-child
                    notification
                    has-background-black has-shadow
                    py-5
                  "
                >
                  <p class="title">Stats</p>
                  Currently running <b>{{ guildsCount }}</b> Servers and
                  watching <b>{{ usersCount }} </b> Users
                  <br />
                  <br />
                  People have run <b>98,765</b> commands today
                </article>
              </div>
            </div>
            <div id="nav-tile" class="tile is-parent is-vertical">
              <nuxt-link :to="{ path: '/wiki' }">
                <article
                  id="nav-child"
                  class="tile is-child notification is-primary"
                >
                  <p class="title">Feature Packed</p>
                  <div class="content subtitle">
                    <ul>
                      <li><b>Moderation</b></li>
                      <ul>
                        <li>Banning</li>
                        <li>Muting</li>
                        <li>Warning</li>
                      </ul>
                      <li><b>Custom Prefixes</b></li>
                      <li><b>User and Message Logging</b></li>
                      <li><b>Role Management</b></li>
                      <li><b>Welcome Messages</b></li>
                      <li><b>Custom Tags</b></li>
                    </ul>
                  </div>
                </article>
              </nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body">
        <div class="tile is-ancestor">
          <div class="tile is-vertical">
            <div id="nav-tile" class="tile is-parent">
              <a
                href="https://discord.com/api/oauth2/authorize?client_id=710672266245177365&permissions=1543630070&scope=bot"
              >
                <div class="columns">
                  <article
                    id="nav-child"
                    class="tile is-child notification is-primary column"
                  >
                    <p class="title">Message Logging</p>
                    <p class="subtitle">
                      Complete message edit and deletion logging to make
                      moderating easy
                    </p>
                  </article>
                  <div id="nav-child">
                    <b-image
                      class="column"
                      src="FeatureImages/MessageEdit.png"
                    />
                  </div>
                </div>
              </a>
            </div>
            <div id="nav-tile" class="tile is-parent has-shadow"></div>
          </div>
        </div>
      </div>
      <a href="https://github.com/ClemBotProject/ClemBot">
        <div id="nav-tile" class="tile is-parent">
          <article id="nav-child" class="tile is-child notification is-dark">
            <p class="title">Open Source</p>
            <p class="subtitle">
              MIT licensed with an active and helpful community
            </p>
          </article>
        </div>
      </a>
    </section>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

interface GlobalStats {
  guilds: string
  users: string
}

export default Vue.extend({
  data() {
    return {
      guildsCount: 'Unknown',
      usersCount: 'Unknown',
    }
  },

  async fetch() {
    const stats: GlobalStats = await fetch(
      'https://localhost:5001/api/public/globalstats'
    ).then((res) => res.json())

    this.guildsCount = stats.guilds ?? 'many'
    this.usersCount = stats.users ?? 'all the'
  },
})
</script>

<style scoped>
.add-to-discord {
  background: #5865f2;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
  text-decoration: none;
}

#splash-card {
  opacity: 0.9;
}

#splash-image {
  box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
  background-image: url('static/SplashBkg.svg');
  background-repeat: no-repeat;
  transform: translatez(0);
  -webkit-transform: translatez(0);

  background-position: bottom;
}

#nav-tile {
  -webkit-transition: all 0.1s ease-in-out;
  -moz-transition: all 0.1s ease-in-out;
  -ms-transition: all 0.1s ease-in-out;
  -o-transition: all 0.1s ease-in-out;
  transition: all 0.1s ease-in-out;
}

#nav-tile :hover {
  -webkit-transition: all 0.1s ease-in-out;
  -moz-transition: all 0.1s ease-in-out;
  -o-transition: all 0.1s ease-in-out;
  transition: all 0.1s ease-in-out;
  -ms-transform: scale(1.015, 1.015);
  /* IE 9 */
  -webkit-transform: scale(1.015, 1.015);
  /* Safari */
  transform: scale(1.015, 1.015);
}

#nav-child :hover {
  transition: none;
  transform: none;
}
</style>
