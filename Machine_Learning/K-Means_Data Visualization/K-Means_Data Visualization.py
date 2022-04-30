import pygame
from random import randint
import math
from sklearn.cluster import KMeans

def distance(p1,p2):
	return math.sqrt((p1[0]-p2[0]) * (p1[0]-p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

pygame.init()

screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("kmeans visualization")
running = True
clock = pygame.time.Clock()

BACKGROUND = (214,214,214)
BLACK = (0,0,0)
BACKGROUND_PANEL = (249,255,230)
WHITE = (255,255,255)

RED = (255,0,255)
GREEN  = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,153,35)
PURPLE = (100,100,100)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLORS = [RED,GREEN, BLUE,YELLOW,PURPLE,ORANGE,GRAPE,GRASS]

font = pygame.font.SysFont('sans',40)
font_small = pygame.font.SysFont('sans',20)

text_plus = font.render('+',True,WHITE)
text_minus = font.render('-',True,WHITE)
text_run = font.render('Run',True,WHITE)
text_random = font.render('Random',True,WHITE)
text_algorithm = font.render('Algorithm',True,WHITE)
text_reset = font.render('Reset',True,WHITE)

points = []
K = 0
error = 0
clusters = []
labels = []
while running:
	clock.tick(60)
	screen.fill(BACKGROUND)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	# Draw interface 

	#draw panel
	pygame.draw.rect(screen,BLACK,(50,50,700,500))
	pygame.draw.rect(screen,BACKGROUND_PANEL,(55,55,690,490))

	# draw button +
	pygame.draw.rect(screen,BLACK,(850,50,50,50))
	screen.blit(text_plus,(865,50))	

	# draw button -
	pygame.draw.rect(screen,BLACK,(950,50,50,50))
	screen.blit(text_minus,(970,48))

	# draw button RUN
	pygame.draw.rect(screen,BLACK,(850,150,150,50))
	screen.blit(text_run,(900,150))	

	# draw button Random
	pygame.draw.rect(screen,BLACK,(850,250,150,50))
	screen.blit(text_random,(865,250))	

	# draw button Algorithm
	pygame.draw.rect(screen,BLACK,(850,450,150,50))
	screen.blit(text_algorithm,(855,450))	

	# draw button Reset
	pygame.draw.rect(screen,BLACK,(850,550,150,50))
	screen.blit(text_reset,(880,550))	

	# draw k 
	text_k = font.render("K = " + str(K),True,BLACK)
	screen.blit(text_k,(1050,50))

	# draw error
	

	# draw small point 
	if 50 < mouse_x < 750 and 50 < mouse_y < 550:
		text_mouse = font_small.render("(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")",True,BLACK)
		screen.blit(text_mouse,(mouse_x + 10,mouse_y + 10))


	# End draw interface


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN:

			# creat point in panel
			if 50 < mouse_x < 750 and 50 < mouse_y < 550:
				labels = []
				point = [mouse_x - 50, mouse_y - 50]
				points.append(point)

			# Draw plus button
			if 850 < mouse_x < 900 and 50 < mouse_y < 100:
				if K < 8:
					K += 1

			# Draw minus button
			if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
				if K > 0:
					K -= 1

			# Draw run button
			if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
				labels = []
				for p in points:
					distances_to_clusters = []
					for c in clusters:
						dis = distance(p,c)
						distances_to_clusters.append(dis)

					min_distances = min(distances_to_clusters)
					label = distances_to_clusters.index(min_distances)
					labels.append(label)

				#update cluster
				for i in range(K):
					sum_x = 0
					sum_y = 0
					count = 0
					for j in range(len(points)):
						if labels[j] == i:
							sum_x += points[j][0]
							sum_y += points[j][1]
							count += 1
					if count != 0:
						clusters[i] = [sum_x / count,sum_y / count]


			# Draw random button
			if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
				clusters = []
				for i in range(K):
					random_point = (randint(0,700), randint(0,500))
					clusters.append(random_point)

			# Draw al button
			if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
				try:
					kmeans = KMeans(n_clusters=K).fit(points)
					labels = kmeans.predict(points)
					clusters = kmeans.cluster_centers_
				except:
					print("error")

			#Draw reset button
			if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
				points = []
				K = 0
				error = 0
				clusters = []
				labels = []

	# Draw clusters
	for i in range(len(clusters)):
		pygame.draw.circle(screen,COLORS[i],(int(clusters[i][0]) + 50,int(clusters[i][1]) + 50), 10)

	# Draw point 
	for i in range(len(points)):
		pygame.draw.circle(screen,BLACK,(points[i][0] + 50,points[i][1] + 50), 6)
		if labels == []:
			pygame.draw.circle(screen,WHITE,(points[i][0] + 50,points[i][1] + 50), 5)	
		else:
			pygame.draw.circle(screen,COLORS[labels[i]],(points[i][0] + 50,points[i][1] + 50), 5)	
	
	# caculate error
	error = 0
	if clusters != [] and labels != []:
		for i in range(len(points)):
			error += distance(points[i],clusters[labels[i]])

	text_k = font.render("Error = " + str(int(error)),True,BLACK)
	screen.blit(text_k,(850,350))

	pygame.display.flip()

pygame.quit()
