import replicate

input = {
    "image": "https://replicate.delivery/pbxt/NkBviX3RzjayD18NeSzeMjZzWZ6eIowQLUDFzGn855TQj0SmA/output.png"
}

output = replicate.run(
    "lucataco/remove-bg:95fcc2a26d3899cd6c2691c900465aaeff466285a65c14638cc5f36f34befaf1",
    input=input
)
print(output)
#=> "https://pbxt.replicate.delivery/NhgojYipuz4WOF16IaGDhQFe...