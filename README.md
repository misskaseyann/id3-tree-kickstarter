# Decision Tree: Mushroom Classification
ID3 decision tree made to determine whether a mushroom is poisonous or not.

### Approach, Metrics, Problems, Experiments, Etc.
All the logic is in one file which reads in the data and then grows the tree utilizing entropy and gain. There is a cut off implemented based on how deep I would like the tree to go so that the program doesn't run forever and fit to the data. Afterwards I pruned the tree based on how well it did when I increased the depth.

There were two datasets I primarily worked on. The first being the mushroom classifier dataset found at the UCI Machine Learning Repository. It is a dataset that determines whether a species of mushroom is definitely edible or definitely poisonous. It was a good dataset to work on since all its attributes had discrete variables which made coding the ID3 program much easier. The data is hypothetical and not drawn from the real world.

I also worked on a smaller dataset taken from the Cards Against Humanity Pulse of the Nation survey results. I downloaded this dataset from Kaggle and eliminated some of the useless information and focused mostly on the demographics of the individuals. Using this information, I thought it would be fun to see if I can classify whether a person has eaten a Kale Salad before.

One of the problems I ran into with this project was the length of time it took to develop a decision tree. I originally developed the code to over fit the data and then utilize post-pruning in order to get the right model but it would take over a day to get me anywhere. I had a hard time trying to utilize some of the pre-pruning rules, so I decided to use a method that was discussed in the class which was to cut off the tree at certain threshold value. I allowed the tree growing function to take in the threshold number and as it recursively called itself, it would increment how deep in the recursion it currently was. Once the algorithm reached the threshold given, it would return a leaf and not a node. This cut the time down exponentially. One other trick I used to cut the tree short in its creation is to check and see if there is only one class being represented in the feature being observed. If there was only one, the algorithm would return a leaf of that class. I also created a threshold on how much a certain class dominated over the other. If the ratio was greater than this threshold, I would return this value as a leaf instead of continuing the recursion.

<img src="http://i65.tinypic.com/121vqkk.png" width=600/>

Once I was able to solve the time issue, I ran into a problem with my mushroom dataset that I was not expecting… one of the features almost completely described the data. No matter how much I modified the thresholds, mushroom odor ultimately determined whether it was edible or poisonous. The classifier, when running the test data against its model, would get an accuracy of 98%. This is great news! However, my tree looks pitiful and simple (see Figure 2). Being unsatisfied with the size and simplicity of my decision tree, I decided to modify the mushroom data by eliminating the odor feature to see what happened. My trees got much more interesting by doing this. In order of recursion depth: level 0 was 18.1% correct, level 1 was 77.4% correct, level 2 and level 3 were 77% correct. Although it is nowhere near as good as the previous model, it was interesting to see the resulting tree without that dominating feature.

Out of curiosity, I experimented with the smaller data set from Cards Against Humanity. This set had no actual final classification and I was more just looking to experiment with the decision trees ability to find correlations in data for the prediction of something as random as eating a kale salad. In order of recursion depth: level 0 was 59% correct, level 1 was 54% correct, level 2 was 60% correct. In my personal opinion, this is not bad for survey data based on stranger’s opinions. It is better than random.

### Effectiveness of the Final Classifiers

For the mushroom classifier that included the feature of odor, it had an accuracy of 98% correct out of 2,125 total data points. The mushroom classifier, without the odor feature, had an accuracy of 77% correct out of the 2,125 total data points. The kale eater’s classifier had a low accuracy of 60% correct out of 201 data points. The greatest success of all these is clearly the original mushroom classifier that identified odor as the dominant feature.

### Final Decision Tree for Mushroom Classifier V.1 and V.2

<img src="http://i63.tinypic.com/kcc9jr.png" width=400/> <img src="http://i64.tinypic.com/2ed5csi.png" width=400/>

### Final Decision Tree for Kale Salad Eaters Classifier
Note: This tree was too complicated to draw on my computer, so I have provided rule based if then pseudo code:
```
What is your highest level of education?
	If College Degree:
		What is your race?
			If White:
				Yes
			If Latino:
				Do you approve of Donald Trump?
					If N/A:
						Unknown
					If Disapprove or Approve:
						No
			If Other:
				Yes
			If Black:
				Do you approve of Donald Trump?
					If Disapprove:
						Yes
					If Approve or N/A:
						No
			If N/A:
				Yes
			If Asian:
				Do you approve of Donald Trump?
					If Approve:
						Yes
					If Disapprove or N/A:
						No
	If Some College:
		What is your gender?
			If Female:
				Have you ever gone hunting?
					If No:
						No
					If Yes:
						Yes
			If Male:
				What is your race?
					If White or Other:
						Yes
					If Latino or Black or Asian or N/A:
						No
			If Other:
				Yes
			If N/A:
				Do you approve of Donald Trump?
					If Approve:
						N/A
					If Disapprove:
						Yes
	If Other:
		What is your race?
			If White or Black or N/A:
				Yes
			If Latino or Asian:
				No
	If Graduate Degree:
		What is your race?
			If Black or White or Latino:
				Yes
			If Asian:
				No
			If Other:
				Have you ever gone hunting?
					If No:
						Yes
					If Yes or N/A:
						No
			If N/A:
				Do you approve of Donald Trump?
					If N/A:
						No
					If Approve or Disapprove:
						Yes
	If High School:
		No
	If N/A:
		Do you approve of Donald Trump?
			If N/A:
				Yes
			If Approve:
				No
```
### Analysis and Discussion
The mushroom dataset that I used was very interesting because it had one specific feature that efficiently described the dataset. Even though the dataset is “fictitious”, it is based off of true findings, so it is in the realm of possibility that a deadly mushroom could be identified by how it smells. However, I wouldn’t go sniffing mushrooms in the woods and then eating them. Outside of the real life danger of eating random mushrooms, this decision tree could be used in an application for mushroom hunters. If a user is venturing deep into the woods and spots a tasty looking shroom, they can use the app to list out identifying features such as smell, shape, and color, in order to get an answer as to whether it’s edible or not. 

The “Kale Eaters Classifier” was created out of a random survey dataset during the presidential season. As an experiment, I thought it would be interesting to see if a decision tree could actually identify some correlations while attempting to classify whether an individual has eaten a kale salad or not. The percentage of success wasn’t the greatest (60%) but I enjoyed seeing how the random data could be clustered together by the algorithm. There were a lot of N/A answers which I strongly believe affected the outcome of each subtree but if I eliminated them from the dataset, I would have too small of a training set. Without N/A answers, I strongly believe I would have greater correlations between the political beliefs of Trump and whether or not the person has eaten a kale salad before.

### Additional Thoughts

The one challenging part of this project was finding a useful dataset. I realize now that data collection is the most difficult and pivotal thing in machine learning projects. If the dataset isn’t accurate or large enough, it can really make life that much more difficult. 
