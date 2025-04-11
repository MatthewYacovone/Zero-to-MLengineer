import numpy as np

# Define the dataset
X_train = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0],
    [1, 1, 0],
])

Y_train = ['Y', 'N', 'Y', 'Y']

X_test = np.array([[1, 1, 0]])

def get_label_indices(labels):
    """
    Group samples based on their labels and return indicies
    @param labels: list of labels
    @return: dict, {class1: [indicies], class2: [indicies]}
    """
    from collections import defaultdict
    label_indices = defaultdict(list)
    for idx, label in enumerate(labels):
        label_indices[label].append(idx)
    return label_indices

label_indices = get_label_indices(Y_train)
print('label_indicies:\n', label_indices)

def get_prior(label_indices):
    """
    Compute prior based on training samples
    @param label_indicies: grouped sample indicies by class
    @return: dictionary, with classs label as key, corresponding prior as value
    """
    prior = {label: len(indices) for label, indices in label_indices.items()}

    total_count = sum(prior.values())

    for label in prior:
        prior[label] /= total_count
    
    return prior

prior = get_prior(label_indices)
print('prior:', prior)

def get_likelihood(features, label_indices, smoothing=0):
    """
    Compute likelihood based on training samples
    @param features: matrix of features
    @param label_indicies: grouped sample indicies by class
    @param smoothing: integer, additive smoothing parameter
    @return: dictionary, with class label as key, corresponding condtional
             probability P(feature|class) vector as value
    """

    likelihood = {}
    for label, indices in label_indices.items():
        likelihood[label] = features[indices, :].sum(axis=0) + smoothing

        total_count = len(indices)
        likelihood[label] = likelihood[label] / (total_count + 2 * smoothing)
    
    return likelihood

smoothing = 1
likelihood = get_likelihood(X_train, label_indices, smoothing)
print('likelihood:\n', likelihood)

def get_posterior(X, prior, likelihood):
    """
    Compute posterior of testing samples, based on prior and likelihood
    @param X: testing samples
    @param prior: dictionary, class label as key, 
            corresponding prior as value
    @param: likelihood: dictionary, with class label as key,
            corresponding conditoinal probability vector as value
    @return: dictionary, with class label as key, corresponding posterior as value
    """
    posteriors = []
    for x in X:
        # posterior is proportional to prior * likelihood
        posterior = prior.copy()
        for label, likelihood_label in likelihood.items():
            for index, bool_value in enumerate(x):
                posterior[label] *= likelihood_label[index] if bool_value else (1 - likelihood_label[index])
        # normalize posterior so that all sums up to 1
        sum_posterior = sum(posterior.values())
        for label in posterior:
            if posterior[label] == float('inf'):
                posterior[label] = 1.0
            else:
                posterior[label] /= sum_posterior
        posteriors.append(posterior.copy())
    return posteriors

posterior = get_posterior(X_test, prior, likelihood)
print('posterior:\n', posterior)



