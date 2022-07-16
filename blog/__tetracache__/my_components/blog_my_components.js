import add_post from "../../components.py__add_post.js";

(() => {
  let __script = add_post;
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/my_components/add_post/_refresh"]}, {"name": "add_post", "endpoint": ["/tetra/blog/my_components/add_post/add_post"]}];
  let __serverProperties = ["key", "title", "content"];
  let __componentName = 'blog__my_components__add_post';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();