import torch

class TensorCalculator():
    def __init__(self):
        pass
# Returns an all-Zeros Tensor
    def zeros_tensor(shape):
        return torch.zeros(shape)


    # Returns an all-Ones Tensor
    def ones_tensor(shape):
        return torch.ones(shape)


    # Returns a Tensor with random values
    def random_tensor(shape):
        return torch.rand(shape)


    # Returns the sum of two tensors
    def add_tensors(tensor1, tensor2):
        if tensor1.shape != tensor2.shape:
            raise ValueError("Tensor shapes must match for addition.")
        return tensor1 + tensor2


    # Returns the multiplication of two tensors
    def multiply_tensors(tensor1, tensor2):
        if tensor1.shape != tensor2.shape:
            raise ValueError("Tensor shapes must match for multiplication.")
        return tensor1 * tensor2

    def divide_tensor(tensor1, tensor2):
        if tensor1.shape != tensor2.shape:
            raise ValueError("Tensor shapes must match for division.")
        return tensor1/tensor2

if __name__ == "__main__":
    # Example usage
    shape = (3, 3)

    zeros = TensorCalculator.zeros_tensor(shape)
    ones = TensorCalculator.ones_tensor(shape)
    random = TensorCalculator.random_tensor(shape)


    tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor2 = torch.tensor([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    result_sum = TensorCalculator.add_tensors(tensor1, tensor2)
    result_multiply = TensorCalculator.multiply_tensors(tensor1, tensor2)
    result_divide = TensorCalculator.divide_tensor(tensor1, tensor2)
    divide = TensorCalculator.divide_tensor(tensor1,tensor2)

    print("Zeros Tensor:")
    print(zeros)
    print("Ones Tensor:")
    print(ones)
    print("Random Tensor:")
    print(random)
    print("Sum of Tensors:")
    print(result_sum)
    print("Product of Tensors:")
    print(result_multiply)
    print("Divide of Tensors:")
    print(result_divide)
