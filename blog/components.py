from sourcetypes import javascript, css, django_html
from tetra import Component, public, Library
from .models import Post

default = Library()

@default.register
class AddPost(Component):
    title=public("")
    content=public("")

 
    def load(self):
        self.post = Post.objects.filter(id=0)


    @public
    def add_post(self, title, content):
        post = Post(
            title = title,
            content = content
        )
        post.save()
       
       

    template: django_html = """
   
    <div class="container">
        <h2>Add blog post</h2>
        <label> Title
        <em>*</em>
        </label>
        <input type="text" maxlength="255" x-model="title" name="title" placeholder="Input post title" required/>

        <label> Content
        <em>*</em>
        </label>
        <textarea rows="20" cols="80" x-model="content" name="content" placeholder="Input blog content" required /> </textarea>

        <button type="submit" @click="addPost(title, content)"><em>Submit</em></button>
    </div>
    
    """

    style: css = """
    .container {
        display: flex;
        flex-direction: column;
        align-items: left;
        justify-content: center;
        border-style: solid;
        width: fit-content;
        margin: auto;
        margin-top: 50px;
        width: 50%;
        border-radius: 15px;
        padding: 30px;
    }

    input, textarea, label{
        margin-bottom: 30px;
        margin-left: 20px;
        ;
    }

    label {
        font-weight: bold;
    }

    input{
        height: 40px;
    }

    h2 {
        text-align: center;
    }

    button {
        width: 150px;
        padding: 10px;
        border-radius: 9px;
        border-style: none;
        background: green;
        color: white;
        margin: auto;
    }

    """

    script: javascript = """
    export default {

        addPost(title, content){
            this.add_post(title, content)   
        }
        
    }
    """


@default.register
class ViewPost(Component):

    def load(self):
        self.posts = Post.objects.all()

    template: django_html = """
        <div>
            <h1> Tetra blog </h1>
            <div class="navbar-nav">
                <a class="nav-item nav-link" href="{% url 'add-post' %}">New Post</a>
            <div>
            <div class="list-group">
                {% for post in posts %}
                    {% @ post_item post=post key=post.id / %}
                {% endfor %}
            </div>
         </div>
        """

@default.register
class PostItem(Component):
   
    def load(self, post):
        self.post = post
        
   
    template: django_html = """
   
    <article class="post-container" >
            <small class="article-metadata">{{ post.date_posted.date}}</small>
            <p class="article-title"><a href="{% url 'post-detail' pk=post.id %}"> {{ post.title }}</a></p>
            <p class="article-content">{{ post.content }}</p>

        </article>
			
    """    

    style: css = """
    
    .article-metadata {
        padding-bottom: 1px;
        margin-bottom: 4px;
        border-bottom: 1px solid #e3e3e3;
        
    }


    .article-title{
        font-size: x-large;
        font-weight: 700;
    }

    .article-content {
        white-space: pre-line;
    }

    .post-container{
        margin: 50px;
    }

    a.article-title:hover {
        color: #428bca;
        text-decoration: none;
    }

    .article-content {
        white-space: pre-line;
    }

    a.nav-item{
        text-align: right;
        margin-right: 100px;
    }

    h1 {
       text-align: center;
    }
    """


@default.register
class PostDetail(Component):
 
    def load(self, pk):
        self.post = Post.objects.filter(id=pk)[0]

    @public(update=False)
    def delete_item(self):
        Post.objects.filter(id=self.post.id).delete()
        self.client._removeComponent()


    template: django_html = """
        <article  {% ... attrs %} > 
            <small class="text-muted">{{ post.date_posted.date}}</small>
                
            <h2 class="article-title">{{ post.title }}</h2>
            <p class="article-content">{{ post.content }}</p>

            <div class="post-buttons">
            <button id="delete-button" type="submit" @click="delete_item()"><em>Delete</em></button>
            <a class="nav-item nav-link" href="{% url 'update-post' pk=post.id %}"><button id="update-button"> <em>Update</em> </button></a>

            </div>
           
        </article>
    """

    style: css = """

        article{
            margin: 100px;
        }

        .post-buttons{
            position: absolute;
            right: 0;
        }

        #delete-button, #update-button{
            width: 150px;
            padding: 10px;
            border-radius: 9px;
            border-style: none;
            font-weight: bold;
            margin: auto;
        }

        #update-button{
            background: blue;
            color: white;
        }

        #delete-button{
            background: red;
            color: white;
        }

    """

@default.register
class PostUpdate(Component):
    title=public("")
    content=public("")


    def load(self, pk):
        self.post = Post.objects.filter(id=pk)[0]
        self.title=self.post.title
        self.content=self.post.content

    @public
    def update_post(self, title, content):
        self.post.title = title
        self.post.content = content

        self.post.save()
        self.title = ""
        self.content = ""

    template: django_html = """
        <div class="container">
            <h2>Update blog post</h2>
            <label> Title
            <em>*</em>
            </label>
            <input type="text" maxlength="255" x-model="title" name="title" placeholder="Input post title" required/>

            <label> Content
            <em>*</em>
            </label>
            <textarea rows="20" cols="80" x-model="content" name="content" placeholder="Input blog content" required> </textarea>

            <button type="submit" @click="update_post(title, content)"><em>Submit</em></button>
        </div>
        """