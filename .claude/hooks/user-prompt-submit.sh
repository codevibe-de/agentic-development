#!/bin/bash
input=$(cat)
mkdir -p "$(dirname "$0")/../../tmp"
echo "$input" | jq . > "$(dirname "$0")/../../tmp/user-prompt-submit-$(date +%s%N).json"
echo "$input" | jq -c '{systemMessage: ("UserPromptSubmit hook input: " + tostring)}'
