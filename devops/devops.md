# src

## Development

```bash
docker-compose -f docker-compose.dev.yml up
```

```bash
# docker-compose -f docker-compose.yml up
# 运行单个服务
# docker-compose up <service-name>
# ME_CONFIG_MONGODB_SERVER: mongo 这是一种错误的写法，这种写法尝试给 ME_CONFIG_MONGODB_SERVER 变量赋值为 mongo，而不是使用环境变量的值这将被视为不完整的（无效的）YAML文件，因为键名没有分配任何内容，可能会导致配置出现问题。
# = 用于分配值，而 : 用于设置默认值
```