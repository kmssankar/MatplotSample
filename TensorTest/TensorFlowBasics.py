import tensorflow as tf

# Create 2 constants

A = tf.constant([[5,2],[11,7]])
B = tf.constant([[3,2],[11,5]])

C = tf.multiply(A,B)
# with open and close Session

# execute TF  using running and closing the session
sessionL = tf.Session()
resultL = sessionL.run(C)
print("With Traditional Run Session ", resultL)
sessionL.close()

# execute TF  using with session
with tf.Session() as session:
      result = session.run(C)
      print("With execution using With Session" , result)