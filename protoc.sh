rm -rf generated/*
protoc --plugin=/home/sijunliu/.pyenv/versions/gapic3.7/bin/protoc-gen-python_gapic -I./api-common-protos -I./google --python_gapic_out=./generated --python_gapic_opt="comma,delimited,options=True" ./google/showcase/v1beta1/*.proto
