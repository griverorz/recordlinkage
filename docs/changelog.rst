*************
Release notes
*************

Version 0.5
===========

- Batch comparing added. Signifant speed improvement.
- rldatasets are now included in the package itself.
- Added an experimental gender imputation tool. 
- Blocking and SNI skip missing values
- No longer need for different index names
- FEBRL datasets included
- Unit tests for indexing and comparing improved
- Documentation updated

Version 0.4
===========

- Fixes a serious bug with deduplication.
- Fixes undesired behaviour for sorted neighbourhood indexing with missing values.
- Add new datasets to the package like Febrl datasets
- Move Krebsregister dataset to this package. 
- Improve and add some tests
- Various documentation updates 

Version 0.3
===========

- Total restructure of compare functions (The end of changing the API is close to now.)
- Compare method ``numerical`` is now named ``numeric`` and ``fuzzy`` is now named ``string``.
- Add haversine formula to compare geographical records. 
- Use numexpr for computing numeric comparisons.
- Add step, linear and squared comparing.
- Add eye index method.
- Improve, update and add new tests.
- Remove iterative indexing functions. 
- New add chunks for indexing functions. These chunks are defined in the class Pairs. If chunks are defined, then the indexing functions returns a generator with an Index for each element.
- Update documentation.
- Various bug fixes.


Version 0.2
===========

- Full Python3 support
- Update the parameters of the Logistic Regression Classifier manually. In literature, this is often denoted as the **deterministic record linkage**.
- Expectation/Conditional Maximization algorithm completely rewritten. The performance of the algorithm is much better now. The algorithm is still experimental.
- New string comparison metrics: Q-gram string comparing and Cosine string comparing. 
- New indexing algorithm: Q-gram indexing.
- Several internal tests.
- Updated documentation.
- BernoulliNBClassifier is now named NaiveBayesClassifier. No changes to the algorithm.
- Arguments order in compare functions corrected.
- Function to clean phone numbers
- Return the result of the classifier as index, numpy array or pandas series. 
- Many bug fixes

Version 0.1
===========
- Official release