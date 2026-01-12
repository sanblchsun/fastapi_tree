from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Company

async def get_companies_tree(session: AsyncSession):
    result = await session.execute(
        select(Company)
    )
    return result.scalars().unique().all()
