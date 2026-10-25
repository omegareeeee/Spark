import os
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.orm import Session
from app.features.ideas.schemas import IdeaIn, CommentIn


from app.core.embeddings import embed

from app.models import Idea
from app.models import Comment

from app.features.map import layout
from app.features.cluster.service import assign_cluster




class service():

    def get_idea(self, db:Session, idea_id: UUID):
        statement = select(Idea).filter_by(id = idea_id)
        return db.scalar(statement)


    def create_idea(self, db: Session, data: IdeaIn):
        vec = embed(f"Title: {data.title}\nDescription: {data.description}")

        #TODO IMPLEMENT LAYOUT AND TRANSFORM
        x = y = None

        if os.path.exists(layout.MODEL_PATH):
            x,y = layout.transform(vec)

        cluster_id = assign_cluster(db, vec)

        idea = Idea(
            # person_id=person_id,
            title = data.title,
            description=data.description,
            github_url=data.github_url,
            idea_embedding=vec,
            author_name=data.author_name,
            x=x,
            y=y,
            cluster_id=cluster_id,
        )

        db.add(idea)
        db.commit()
        db.refresh(idea)

        return self.get_idea(db, idea.id)

    
    def get_all_ideas(self, db: Session):
        statement = select(Idea).order_by(Idea.created_at.desc())
        return db.scalars(statement).all()

    def like_idea(self, db: Session, idea_id: UUID):
        result = db.execute(
            update(Idea).where(Idea.id == idea_id)
            .values(like_count=Idea.like_count + 1)
            .returning(Idea.like_count)
        ).scalar()
        db.commit()
        return result 