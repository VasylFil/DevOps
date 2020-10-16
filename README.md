# lbs
#### Lab_1:
* `git clone` [`link`](https://github.com/vasylfil/lbs.git) - this command is used for downloading git repo to your current working directory;

Previous commit's hash: `fee6b4a60a2e08ae5ded4990eb2c477623cf2dac`
* `git log` - is used for showing all commits in the current branch’s history;
* `git branch [branch_name]` allows to create a new branch;
* `git checkout [branch_name]` allows to switch between branches;

Previous push failed since `new_branch` had no upsteam branch. To fix it `git push` requires some additional arguments `--set-upstream origin new_branch
` to be specified.