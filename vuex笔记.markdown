# Getting Started
There are two things that make a Vuex store different from a plain global object:

1.Vuex stores are reactive. When Vue components retrieve state from it, they will reactively and efficiently update if the store's state changes.

2.You cannot directly mutate the store's state. The only way to change a store's state is by explicitly committing mutations. This ensures every state change leaves a track-able record, and enables tooling that helps us better understand our applications.