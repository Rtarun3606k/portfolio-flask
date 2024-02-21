from google.protobuf import any_pb2

# Assuming you have the protocol buffer definition
# Replace 'YourProtoMessage' with the actual name of your message class
proto_message = """"block_reason: SAFETY\nsafety_ratings {\n  category: HARM_CATEGORY_SEXUALLY_EXPLICIT\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HATE_SPEECH\n  probability: NEGLIGIBLE\n}\nsafety_ratings {\n  category: HARM_CATEGORY_HARASSMENT\n  probability: HIGH\n}\nsafety_ratings {\n  category: HARM_CATEGORY_DANGEROUS_CONTENT\n  probability: HIGH\n}\n"""

# Parse the binary string
binary_string = b"\x08\x01\x12\x04SAFE\x10\x00"
proto_message.ParseFromString(binary_string)

# Access the values
for safety_rating in proto_message.safety_ratings:
    print("Category:", safety_rating.category)
    print("Probability:", safety_rating.probability)