﻿using ClemBot.Api.Common;
using ClemBot.Api.Data.Contexts;
using Microsoft.EntityFrameworkCore;

namespace ClemBot.Api.Core.Features.Reminders.Bot;

public class FetchAll
{
    public class ReminderDto : IResponseModel
    {
        public int Id { get; set; }

        public DateTime Time { get; set; }
    }

    public class Query : IRequest<IQueryResult<List<ReminderDto>>>
    {
        // empty
    }

    public record Handler(ClemBotContext _context) : IRequestHandler<Query, IQueryResult<List<ReminderDto>>>
    {
        public async Task<IQueryResult<List<ReminderDto>>> Handle(Query request, CancellationToken cancellationToken)
        {
            var reminders = await _context.Reminders
                .Where(r => !r.Dispatched)
                .Select(item => new ReminderDto {
                    Id = item.Id,
                    Time = item.Time
                })
                .ToListAsync();

            return QueryResult<List<ReminderDto>>.Success(reminders);
        }
    }
}
