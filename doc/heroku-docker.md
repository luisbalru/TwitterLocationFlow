# HEROKU DEPLOYMENT WITH DOCKER

## heroku.yml

Create a heroku.yml manifest from an existing application. To enable these features, switch to the **beta** CLI and install *manifest* plugin:

`$ heroku update beta`  
`$ heroku plugins:install @heroku-cli/plugin-manifest` 

To create a manifest from a existing app:

`$ heroku manifest:create`

## Container Registry & Runtime (Docker Deploys)

[Doc](https://devcenter.heroku.com/articles/container-registry-and-runtime)

### Logging in to the registry

Using Heroku CLI,  

`$ heroku container:login`

### Bulding and pushing images

`$ heroku container:push <process-type>`

Pushing and existing image:   
`$ docker tag <image> registry.heroku.com/<app>/<process-type>`
`$ docker push registry.heroku.com/<app>/<process-type>`

### Releasing an image

`$ heroku container:release web`