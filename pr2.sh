rm -rf pubsub/*
protoc --plugin=/home/sijunliu/.pyenv/versions/gapic/bin/protoc-gen-python_gapic -I./api-common-protos -I./google --python_gapic_out=./pubsub --python_gapic_opt="comma,delimited,options=True" ./google/pubsub/v1/*.proto
