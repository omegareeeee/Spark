import os
from uuid import UUID, uuid4
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.features.ideas.schemas import IdeaIn

from app.core.embeddings import embed

from app.models import Idea

class service():

    def get_idea(self, db:Session, idea_id: UUID):
        statement = select(Idea).filter_by(id = idea_id)
        return db.scalar(statement)


    def create_idea(self, db: Session, data: IdeaIn):
        vec = embed(f"{data.title}. Description{data.description}")

        x,y = 0,0
        cluster_id = 1
        #TODO IMPLEMENT LAYOUT AND TRANSFORM
        # x = y = None

        # if os.path.exists(layout.MODEL_PATH):
        #     x,y = layout.transform(vec)

        # cluster_id = assign_cluster(db, vec)

        idea = Idea(
            # person_id=person_id,
            title = data.title,
            description=data.description,
            github_url=data.github_url,
            idea_embedding=vec,
            x=x,
            y=y,
            cluster_id=None,
        )

        db.add(idea)
        db.commit()
        db.refresh(idea)

        return self.get_idea(db, idea.id)


#  id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     person_id: Mapped[UUID] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"))
#     text: Mapped[str] = mapped_column(Text)
#     idea_embedding = mapped_column(Vector(EMBED_DIM))
#     github_url: Mapped[str | None] = mapped_column(Text, nullable=True)
#     x: Mapped[float | None]
#     y: Mapped[float | None]
#     cluster_id: Mapped[int | None] = mapped_column(ForeignKey("clusters.id"))
#     created_at: Mapped[datetime] = mapped_column(server_default=func.now())