from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.


def backchain_to_goal_tree(rules, hypothesis):
    # print("////BACKCHAINING on hypothesis: " + hypothesis)
    goal_tree = OR(hypothesis)
    for rule in rules:
        # It's given that we can assume the consequent is just THEN(...), so we want what's inside the consequent
        consequents = rule.consequent()[0]
        if not isinstance(consequents, list):
            consequents = AND(consequents)

        # Check if consequents satisfy the hypothesis; if so, we need to backchain on this consequent!
        for consequent in consequents:
            bindings = match(consequent, hypothesis)
            if not bindings is None:
                # We now want to backchain on this rule because it proves what we want!
                antecedent = rule.antecedent()
                if not isinstance(antecedent, list):
                    antecedent = AND(antecedent)
                # print(rule)
                # print(antecedent)
                # print("---")
                # now iterate through antecedent, and for each leaf, recursively backchain again: OR(leaf, backchain tree)
                for i in range(len(antecedent)):
                    antecedent[i] = backchain_to_goal_tree(rules, populate(antecedent[i], bindings))
                goal_tree.append(antecedent)

    return simplify(goal_tree)

# Here's an example of running the backward chainer - uncomment
# it to see it work:
# print(backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin'))
# WHY does having this enabled affect one of the tests? Python is so weird
