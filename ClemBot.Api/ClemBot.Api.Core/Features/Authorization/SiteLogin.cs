using System.Security.Claims;
using System.Threading;
using System.Threading.Tasks;
using ClemBot.Api.Core.Security;
using ClemBot.Api.Core.Security.JwtToken;
using ClemBot.Api.Core.Security.OAuth;
using ClemBot.Api.Core.Utilities;
using ClemBot.Api.Data.Contexts;
using ClemBot.Api.Data.Extensions;
using MediatR;
using Microsoft.AspNetCore.Http;

namespace ClemBot.Api.Core.Features.Authorization;

public class SiteLogin
{
    public class Query : IRequest<Result<Model, AuthorizeStatus>>
    {
        public string Bearer { get; set; } = null!;
    }

    public class Model
    {
        public string Token { get; set; } = null!;
    }

    public class Handler : IRequestHandler<Query, Result<Model, AuthorizeStatus>>
    {
        private readonly ClemBotContext _context;

        private readonly ILogger<Handler> _logger;

        private readonly IHttpContextAccessor _httpContextAccessor;

        private readonly IJwtAuthManager _jwtAuthManager;

        private readonly JwtTokenConfig _jwtTokenConfig;

        private readonly IDiscordAuthManager _discordAuthManager;

        public Handler(ClemBotContext context,
            ILogger<Handler> logger,
            IHttpContextAccessor httpContextAccessor,
            IJwtAuthManager jwtAuthManager,
            JwtTokenConfig jwtTokenConfig,
            IDiscordAuthManager discordAuthManager)
        {
            _context = context;
            _logger = logger;
            _httpContextAccessor = httpContextAccessor;
            _jwtAuthManager = jwtAuthManager;
            _jwtTokenConfig = jwtTokenConfig;
            _discordAuthManager = discordAuthManager;
        }

        public async Task<Result<Model, AuthorizeStatus>> Handle(Query request, CancellationToken cancellationToken)
        {
            _httpContextAccessor.HttpContext!.Request.Headers.TryGetValue("Origin", out var origin);
            _logger.LogInformation("Site Login Request Initialized from Url: {Origin}", origin);
            if (!await _discordAuthManager.CheckTokenIsUserAsync(request.Bearer))
            {
                _logger.LogWarning("Site Login Request Denied: Invalid Token");
                return AuthorizeResult<Model>.Forbidden();
            }

            _logger.LogInformation("Site Login Request Accepted");

            var claims = new[]
            {
                new Claim(Claims.DiscordBearer, request.Bearer)
            };

            _logger.LogInformation("Generating JWT Access Token");
            var token = _jwtAuthManager.GenerateToken(claims, DateTime.Now);
            _logger.LogInformation("JWT Access Token Successfully Generated");

            return AuthorizeResult<Model>.Success(new Model {Token = token});
        }
    }
}
