
## Before starting with rules

We need to create a client directory in here that has:
 - `policy_types.yml`: Each policy type name in there holds the value of that LOB `id` in BriteCore.
 - {policy_types_names}: Those are the names of LOBs that'll fire on agent submission, i.e: `homeowners.py` holds all the rules specifically for that LOB upon submitting a quote. Every name defined in `policy_types.yml` should have an identical python file name under the client dir.

## Defining a Rule

Rules are written as Python methods. Let's take the following example:

```python
@dynamic_defaults
def rule_1(test_category="{{bc::Category::Test Category}}",
           cov_a="{{bc::Item::Coverage A}}",
           list_question="{{bc::Question::Underwriting Questions::List Question}}",
           text_question="{{bc::Question::Underwriting Questions::Text Question}}"):

    if (test_category == "Yes" and cov_a.limit < 100000 and
        list_question != "maybe" and text_question != "No answer provided"):
        return True
    return False
```

* The first thing that all rule methods need is the `dynamic_defaults` decorator. This decorator controls the `kwargs` and the functions will not work without it.
* Rules methods *can* accept `args`, but the functionality is not currently in use. Define all the information that you will need as `kwargs`. You can reference the following things in the normal BC reference style:

  1. Items -- `{{bc::Item::<Item Name>}}` This is an object that has `premium`, `limit` and `deductible` attributes. You can also ensure that the item is not `None` (it exists on the policy).
  2. Categories -- `{{bc::Category::<Category Name>}}` Contains the value of the category in builder as a `str`.
  3. Supplemental Questions -- `{{bc::Question::<Item Name>::<Supplemental Question Name>}}` Also store the value of the question as a `str`.

* The logic required for the rule. Any valid Python is accepted here, although the use of external libraries will need further configuration. In English, the example above the logic says:

  "If Test Category is 'Yes' and the limit of Coverage A is less than 100,000 and the supplemental question 'List Question' in the item 'Underwriting Questions' is not 'maybe' and the supplemental question 'Text Question' in the item 'Underwriting Questions' has been answered, then this rule passes (returns True)"

* Each Rule has an optional `fallback` argument that fallsback to the given value when the _rule reference string_ fails to be resolved into a proper rule object to be executed. This should happen for example if the string references a category or a question that does not exist for the given policy type.
```python
@dynamic_defaults
def pass_when_empty(test="{{bc::Question::Application Questions::Important?}}", fallback=True)
    # If this rule isn't part of the body, then it'll fallback to True
```

*Note:* For Straight-Through Processing to fire, all rules must return `True`.

## Telling a Rule Where To Run

After your rule methods are written, you then need to tell them to run on either risk or policy level. Rules defined at the risk level will run on every risk. (Note that the engine will short circuit on multi-risk policies when one evaluates to False.) This is done by simply adding the Rule to list of either (`risk_rules`, `policy_rules`, `risk_subline_rules`).

```
risk_rules = [
  Rule('Risk Rule 1', rule_1),
  Rule('Risk Rule 2', rule_2),
  Rule('Risk Rule 3', rule_3),
  ....
]
```

`Rule` is a namedtuple that takes a name and the function. This is so you can give rules more dynamic names than the method name allows. Once a rule is added to list above, it will fire on agent submission.

