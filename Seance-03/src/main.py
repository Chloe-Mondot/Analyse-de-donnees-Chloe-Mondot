#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

#dossier de sauvegarde des images
IMG_DIR = "img"

#https://docs.scipy.org/doc/scipy/reference/stats.html

dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

print(dist_names)

# Question 1
print("Question 1")

#LOIS DISCRETES

#fonction de visualisation 
def visualiser_discrete(nom, x, probabilites):

    plt.figure(figsize=(8, 5))

    plt.bar(x, probabilites, color="steelblue",
            edgecolor="black")

    plt.title("Distribution " + nom)

    plt.xlabel("Valeurs")

    plt.ylabel("Probabilités")

    plt.grid(axis="y", alpha=0.3)

#enregistrement de l'image dans le dossier img
    plt.savefig(os.path.join(IMG_DIR, nom + ".png"))

    plt.show()

    plt.close()



#1. Loi de Dirac

dirac = stats.rv_discrete(name='dirac', values=([5], [1]))

x = np.arange(0, 10)
p = dirac.pmf(x)

visualiser_discrete("dirac", x, p)

#2. Loi uniforme discrète

a = 1
b = 10
loi_uniforme = stats.randint(a, b + 1)

x = np.arange(a, b + 1)
p = loi_uniforme.pmf(x)

visualiser_discrete("loi_uniforme", x, p)

#3. Loi binomiale

n = 10
proba = 0.5
loi_binomiale = stats.binom(n, proba)

x = np.arange(0, n + 1)
p = loi_binomiale.pmf(x)

visualiser_discrete("loi_binomiale", x, p)

#4. Loi de Poisson

lambda_param = 3 #nb moyen d'évènements observés
loi_poisson = stats.poisson(lambda_param)

x = np.arange(0, 20)
p = loi_poisson.pmf(x)

visualiser_discrete("loi_poisson", x, p)

#5. Loi de Zipf-Mandelbrot

s = 1.5 #vitesse de décroissance
q = 1 #paramètre de décalage
N = 50 #nombre de valeurs

x = np.arange(1, N + 1) #tableau de 50 valeurs
p = 1 / ((x + q) ** s) #loi de Zipf-M
p = p / np.sum(p) #normalisation des probabilités 

visualiser_discrete("Zipf_mandelbrot", x, p)


#LOIS CONTINUES

def visualiser_continue(nom, distribution):

    # Définir les limites du graphique
    minimum = distribution.ppf(0.001)
    maximum = distribution.ppf(0.999)

    # Créer les valeurs de x
    x = np.linspace(minimum, maximum, 1000)

    # Calculer la densité
    y = distribution.pdf(x)

    # Tracer le graphique
    plt.figure(figsize=(8, 5))

    plt.plot(x, y, color="darkorange")

    plt.fill_between(x, y, alpha=0.2)

    plt.title("Distribution " + nom)

    plt.xlabel("Valeurs")

    plt.ylabel("Densité de probabilité")

    plt.grid(alpha=0.3)

    # Enregistrer le graphique
    plt.savefig(os.path.join(IMG_DIR, nom + ".png"))

    plt.show()

    plt.close()

#1. Loi uniforme continue

a = 0 
b = 10

loi_uniforme_continue = stats.uniform(loc=a, scale=b - a)

visualiser_continue("loi_uniforme_continue", loi_uniforme_continue)

#2.Loi normale

loi_normale = stats.norm(loc=0, scale=1)

visualiser_continue("loi_normale", loi_normale)

#3. Loi log-normale

lognormale = stats.lognorm(s=0.5, scale=np.exp(0))

visualiser_continue("lognormale", lognormale)

#4. Loi du chi-deux

chi2 = stats.chi2(df=5)

visualiser_continue("chi2", chi2)

#5. Loi de Pareto 

pareto = stats.pareto(b=3, scale=1)

visualiser_continue("pareto", pareto)

# Question 2
print("Question 2")
