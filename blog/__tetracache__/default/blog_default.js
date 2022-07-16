import add_post from "../../components.py__add_post.js";

(() => {
  let __script = add_post;
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/default/add_post/_refresh"]}, {"name": "add_post", "endpoint": ["/tetra/blog/default/add_post/add_post"]}];
  let __serverProperties = ["key", "title", "content"];
  let __componentName = 'blog__default__add_post';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();
(() => {
  let __script = {};
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/default/view_post/_refresh"]}];
  let __serverProperties = ["key"];
  let __componentName = 'blog__default__view_post';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();
(() => {
  let __script = {};
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/default/post_item/_refresh"]}];
  let __serverProperties = ["key"];
  let __componentName = 'blog__default__post_item';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();
(() => {
  let __script = {};
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/default/post_detail/_refresh"]}, {"name": "delete_item", "endpoint": ["/tetra/blog/default/post_detail/delete_item"]}];
  let __serverProperties = ["key"];
  let __componentName = 'blog__default__post_detail';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();
(() => {
  let __script = {};
  let __serverMethods = [{"name": "_refresh", "endpoint": ["/tetra/blog/default/post_update/_refresh"]}, {"name": "update_post", "endpoint": ["/tetra/blog/default/post_update/update_post"]}];
  let __serverProperties = ["key", "title", "content"];
  let __componentName = 'blog__default__post_update';
  window.document.addEventListener('alpine:init', () => {
    Tetra.makeAlpineComponent(
      __componentName,
      __script,
      __serverMethods,
      __serverProperties,
    )
  })
})();