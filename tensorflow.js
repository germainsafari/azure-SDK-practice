const tensorA = tf.tensor([[1,2], [3,4], [4,3]])
const tensorB = tf.tensor([[2,-2],[4,3],[5,3]])

const tensorNew = tensorA.add(tensorB)
const tensorNewer = tensorA.sub([[3,5],[3,4],[3,2]])

// train tensorflow.js model to predict Y values based on X inputs
// create training data
const xs = tf.tensor([0,1,2,3,4]);
const ys = xs.mul(1.2).add(5);

//define a linear regression model
const model = tf.sequential();
model.add(tf.layers.dense({units:1, inputShape:[1]}));

//specify loss and optimizer
model.compile({loss:'meansquarterror'})