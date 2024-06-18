const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    // 其他 devServer 配置 ...
    client: {
      webSocketURL: {
        hostname: 'localhost', // 主机名
        pathname: '/ws',
        port: 8080, // 端口号
        protocol: 'wss', // 确保使用 wss 协议
      },
    },
  },
  transpileDependencies: true,
  configureWebpack: {
    resolve: {
      alias: {
        winwheel: 'winwheel/dist/Winwheel.min.js'
      }
    }
  }
})
