using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using ClemBot.Api.Core.Utilities;
using ClemBot.Api.Data.Contexts;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace ClemBot.Api.Core.Features.Public
{
    public class GlobalStats
    {
                public class Query : IRequest<Result<Model, QueryStatus>>
                {
                }

                public class Model
                {
                    public int Guilds { get; set; }

                    public int Users { get; set; }
                }

                public record Handler(ClemBotContext _context) : IRequestHandler<Query, Result<Model, QueryStatus>>
                {
                    public async Task<Result<Model, QueryStatus>> Handle(Query request,
                        CancellationToken cancellationToken)
                    {
                        var guildCount = await _context.Guilds.CountAsync();

                        var userCount = await _context.GuildUser.CountAsync();

                        return QueryResult<Model>.Success(new Model()
                        {
                            Guilds = guildCount,
                            Users = userCount
                        });
                    }
                }

    }
}
