using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Threading.Tasks;
using ClemBot.Api.Core.Security.OAuth.OAuthUser;

namespace ClemBot.Api.Core.Security.OAuth
{
    public class DiscordAuthManager : IDiscordAuthManager
    {
        private readonly IHttpClientFactory _httpClientFactory;

        private const string DISCORD_USER_URL = @"https://discord.com/api/oauth2/@me";

        private const string DISCORD_USER_GUILDS_URL = @"https://discord.com/api/users/@me/guilds";

        public DiscordAuthManager(IHttpClientFactory httpClientFactory)
        {
            _httpClientFactory = httpClientFactory;
        }
        public async Task<bool> CheckTokenIsUserAsync(string bearer)
        {
            using var client = _httpClientFactory.CreateClient();
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", bearer);

            var resp = await client.GetAsync(DISCORD_USER_URL);

            return resp.StatusCode == HttpStatusCode.OK;
        }

        public async Task<DiscordOAuthModel?> GetDiscordUserAsync(string bearer)
        {
            using var client = _httpClientFactory.CreateClient();
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", bearer);

            var resp = await client.GetAsync(DISCORD_USER_URL);

            return await resp.Content.ReadFromJsonAsync<DiscordOAuthModel>();
        }

        public async Task<List<Guild>?> GetDiscordUserGuildsAsync(string bearer)
        {
            using var client = _httpClientFactory.CreateClient();
            client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", bearer);

            var resp = await client.GetAsync(DISCORD_USER_GUILDS_URL);

            return await resp.Content.ReadFromJsonAsync<List<Guild>>();

        }
    }
}