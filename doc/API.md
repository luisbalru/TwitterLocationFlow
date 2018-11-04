# DOCUMENTACIÓN SOBRE LA API
## Funciones

| Método |      URI       |     Parámetros     |                          Return                          |              Función               |
| :----: | :------------: | :----------------: | :------------------------------------------------------: | :--------------------------------: |
|  GET     |       /       |                    |                         "status": `status`                      |         Devuelve el estado de la app |
| GET | /status    |                  |          "status": `status`     | Devuelve el estado de la app |
| POST | /all |     |  \{ `node_i` : [ `edges_i`] \} | Devuelve el grafo completo (json) |
| POST | /vertices |   | \{[`vertex_i`] \} | Devuelve una lista con todos los vértices |
| POST | /aristas |   | \{[`vertex_i vertex_j`] \} | Devuelve una lista con todas las aristas (conjuntos de dos o más vértices) |
| POST | /grado/`<id>` | identificador del vértice `id` | int:`grado_vertex` | Devuelve el grado del vértice `id` |
| POST | /vertices_aislados | |  \{[`vertex-iso_i`] \} | Devuelve una lista con todos los vértices aislados |
| POST | /vertices/add/`<vertex>` | Vértice `vertex` |  | Introduce en memoria el nuevo vértice |
| POST | /aristas/add/`<edge>` | Arista `edge` |  | Introduce en memoria una nueva conexión entre dos vértices existentes |
| DELETE | /vertices/remove/`<vertex>` | Vértice `vertex` |  | Elimina de la estructura de datos el vértice `vertex` |
| DELETE | /aristas/remove/`<edge>` | Arista `edge` (lista con dos vértices) |   | Elimina de la estructura de datos las conexiones entre los dos vértices dados |
