using ClemBot.Api.Common.Security.Policies.BotMaster;
using ClemBot.Api.Data.Contexts;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ClemBot.Api.Core.Features.HealthCheck;

[ApiController]
[Route("api")]
public class HealthCheckController(ClemBotContext context) : ControllerBase
{
    [HttpGet("[controller]/ping")]
    [BotMasterAuthorize]
    public IActionResult Ping() => Ok("pong!");

    [HttpGet("/livez")]
    [AllowAnonymous]
    public IActionResult Live() => Ok(new { status = "ready" });

    [HttpGet("/readyz")]
    [AllowAnonymous]
    public async Task<IActionResult> Ready(CancellationToken cancellationToken)
    {
        try
        {
            await context.Database.OpenConnectionAsync(cancellationToken);
            await context.Database.CloseConnectionAsync();
            return Ok("ready");
        }
        catch (Exception ex)
        {
            return StatusCode(503, new { error = ex.Message });
        }
    }
}
