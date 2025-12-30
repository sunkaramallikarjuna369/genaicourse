"""Day 20: GraphQL APIs with Python
Learn to build GraphQL APIs using Ariadne and handle queries and mutations.
"""

from ariadne import make_executable_schema, QueryType, MutationType, convert_kwargs_to_snake_case
from ariadne.asgi import make_asgi_handler
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import GraphQLRoute
from typing import List, Dict, Any

# Define GraphQL Schema
type_defs = """
    type Query {
        hello: String!
        users: [User!]!
        user(id: ID!): User
        posts(authorId: ID!): [Post!]!
    }

    type Mutation {
        createUser(name: String!, email: String!): User!
        createPost(authorId: ID!, title: String!, content: String!): Post!
        updateUser(id: ID!, name: String): User
        deleteUser(id: ID!): Boolean!
    }

    type User {
        id: ID!
        name: String!
        email: String!
        posts: [Post!]!
    }

    type Post {
        id: ID!
        title: String!
        content: String!
        author: User!
        createdAt: String!
    }
"""

# Sample data storage
users_db: Dict[str, Dict[str, Any]] = {
    "1": {"id": "1", "name": "Alice", "email": "alice@example.com"},
    "2": {"id": "2", "name": "Bob", "email": "bob@example.com"}
}

posts_db: Dict[str, Dict[str, Any]] = {
    "1": {"id": "1", "title": "GraphQL Basics", "content": "Learn GraphQL", "authorId": "1", "createdAt": "2024-01-01"},
}

post_counter = 2
user_counter = 3

# Define resolvers
query = QueryType()
mutation = MutationType()

@query.field("hello")
def resolve_hello(obj, info):
    return "Hello GraphQL World!"

@query.field("users")
def resolve_users(obj, info):
    return list(users_db.values())

@query.field("user")
def resolve_user(obj, info, id):
    return users_db.get(id)

@query.field("posts")
def resolve_posts(obj, info, authorId):
    return [p for p in posts_db.values() if p['authorId'] == authorId]

@query.field("User.posts")
def resolve_user_posts(user, info):
    return [p for p in posts_db.values() if p['authorId'] == user['id']]

@query.field("Post.author")
def resolve_post_author(post, info):
    return users_db.get(post['authorId'])

@mutation.field("createUser")
@convert_kwargs_to_snake_case
def resolve_create_user(obj, info, name, email):
    global user_counter
    new_user = {"id": str(user_counter), "name": name, "email": email}
    users_db[str(user_counter)] = new_user
    user_counter += 1
    return new_user

@mutation.field("createPost")
@convert_kwargs_to_snake_case
def resolve_create_post(obj, info, author_id, title, content):
    global post_counter
    new_post = {
        "id": str(post_counter),
        "title": title,
        "content": content,
        "authorId": author_id,
        "createdAt": "2024-01-15"
    }
    posts_db[str(post_counter)] = new_post
    post_counter += 1
    return new_post

@mutation.field("updateUser")
@convert_kwargs_to_snake_case
def resolve_update_user(obj, info, id, name=None):
    user = users_db.get(id)
    if user and name:
        user['name'] = name
    return user

@mutation.field("deleteUser")
def resolve_delete_user(obj, info, id):
    if id in users_db:
        del users_db[id]
        return True
    return False

# Create executable schema
schema = make_executable_schema(type_defs, query, mutation)

# Create ASGI handler
app = Starlette(routes=[GraphQLRoute("/graphql", schema=schema)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
