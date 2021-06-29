<template>
  <div>
    <section id="splash-image" class="hero">
      <div class="hero-body columns">
        <div class="column is-two-fifths">
          <img
            id="main-logo"
            class="mt-6 is-justify-content-center is-align-content-center"
            src="ClemBotLogo.svg"
            alt="ClemBot"
          />
        </div>
        <div class="card column is-dark mt-6 mr-6">
          <div class="card-content">
            <h1 class="is-size-1 title has-text-white">ClemBot</h1>
            <p class="subtitle has-text-white">
              The modular and configurable open source Discord Bot of the future
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
                  class="tile is-child notification is-primary has-shadow py-5"
                >
                  <p class="title">Stats</p>
                  Currently running <b>12,345</b> Servers and watching
                  <b>56,789</b> Users
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
                  class="tile is-child notification is-info"
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
          <a href="https://github.com/ClemBotProject/ClemBot">
            <div id="nav-tile" class="tile is-parent">
              <article
                id="nav-child"
                class="tile is-child notification is-dark"
              >
                <p class="title">Open Source</p>
                <p class="subtitle">
                  MIT licensed with an active and helpful community
                </p>
              </article>
            </div>
          </a>
        </div>
      </div>
    </section>
    <section class="hero is-fullheight-with-navbar">
      <div class="hero-body">
        <p class="title">Site</p>
      </div>
    </section>
  </div>
</template>

<style scoped>

.add-to-discord {
  background: #5865f2;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
  text-decoration: none;
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
