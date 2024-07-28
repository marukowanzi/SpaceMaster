import replicate

input = {
    "image_path": "https://replicate.delivery/pbxt/KVwdH39PhIC46WaizHYsrFp9f5oLSr65VKhEtxoFtmmwEqeL/hamburger.png",
    "do_remove_background": True
}

output = replicate.run(
    "camenduru/tripo-sr:e0d3fe8abce3ba86497ea3530d9eae59af7b2231b6c82bedfc32b0732d35ec3a",
    input=input
)
print(output)
#=> "https://replicate.delivery/pbxt/X2nbiuc9uX5LM9DP1c0PcbWe...