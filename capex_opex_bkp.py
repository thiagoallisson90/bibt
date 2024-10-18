#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
####################################### 
########### CAPEX ##########
#######################################
'''
CAPEX --> custo de capital
CBs --> custo de aquisição LoraWAN
Cins --> custo de implantação (pagar equipe para ir ao local ou projetar o local para instalar um gateway)
Cset --> custo de configuração do gateway
Txinst --> instalação de transmissão (comunicação gateway-nuvem, depende do local e o aplicativo, e pode ser LTE ou mesmo fibra)
'''
grid_gw25=25
number_gw=22
place_fcm=16
CBs=1
Cins=2
Cset=0.1
Txinst=4

print("grid_gw25: ",grid_gw25)
print("number_gw proposto: ",number_gw)
print("place_fcm: ",place_fcm)

#grid_gw25=23 #numero de gateway rand 25 (pelo grafico considerou 23gw!)
grid_gw25=grid_gw25 #numero de gateway grid 25

gw_fuzzy=number_gw #numero de gateway fuzzy

gateway_place=place_fcm
gw_place=gateway_place #numero de gateway fuzzy

gw_kmeans=number_gw #numero de gateway kmeans

gw_fuzzy=number_gw#numero de gateway fuzzy (numero que está no artigo e tese)
#gw_rand16=rand_gw16
#gw_fuzzy=15 #arredondou  para 15


#----------------------------------------------------
"""
#----------------REDUÇÃO DE 5% gw fuzzy -------------
reducao_fuzzy=1-(15/gw_fuzzy)   #15/15.78==>5%
print("\nReducao FCM (%): ", reducao_fuzzy*100)
print('grid25 =',grid_gw25)
grid=grid_gw25- reducao_fuzzy*grid_gw25 #reduzindo 5% do grid_25
print("novo grid com redução de ",reducao_fuzzy*100,": ", grid)
gw_fuzzy=math.trunc(gw_fuzzy) #trunca 15.78 para 15
grid_gw25=math.trunc(grid) #trunca 23,76 para 23
print("novo grid (com reduzação proprocional): ", grid_gw25)
"""
#----------------------------------------------

#calculo CAPEX
#CAPEX=total_gw*(Cbs + Cins + Cset + Txinst)
capex_grid_gw25=grid_gw25 *(CBs + Cins + Cset + Txinst)
capex_gw_fuzzy= gw_fuzzy * (CBs + Cins + Cset + Txinst)
capex_gw_kmeans= gw_kmeans * (CBs + Cins + Cset + Txinst)
capex_gw_place= gateway_place * (CBs + Cins + Cset + Txinst)
#capex_gw_rand16= gw_rand16 * (CBs + Cins + Cset + Txinst)


print("\n ---------------Dados CAPEX----------------------------\n")
print("Valor capex_grid25: ",capex_grid_gw25)
print("Valor capex_gw_FCM: ",capex_gw_fuzzy)
print("Valor capex_gw_Place_16gw: ",capex_gw_place)
#print("Valor capex_gw_rand16: ",capex_gw_rand16)

resultado_capex=(capex_gw_fuzzy/capex_grid_gw25)
resultado=(1-resultado_capex)*100


resultado_capex_place=(capex_gw_place/capex_grid_gw25)
resultado_place=(1-resultado_capex_place)*100

print("\nPorcentagem CAPEX do fcm/grid25(%): ",resultado)
print("Porcentagem CAPEX do resultado_capex_place/grid25(%): ",resultado_place)

#print('--------------------------------------------------')
#+++++++++++++++++++CAPEX COLORIDO ++++++++++++++++++++++++++
# width=0.4
#nome_proposta='Proposta'
nome_proposta='Proposal'
'''
plt.bar('Grid25', capex_grid_gw25, color =cor_grid25, align='center', width=0.6, hatch = hat_grid25)
#plt.bar('FCM', capex_gw_fuzzy, color = cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
plt.bar(nome_proposta, capex_gw_fuzzy, color = cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
#plt.bar('Comparative_study', capex_gw_fuzzy, color = cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
plt.bar('Place', capex_gw_place, color = cor_place, align='center', width=0.5, hatch = hat_place)
#plt.bar('kmeans', capex_gw_kmeans, color = cor_kmeans, align='center', width=0.5, hatch = hat_kmeans)
#plt.bar('rand16', capex_gw_rand16, color = cor_rand16, align='center', width=0.5, hatch = hat_rand16)

#plt.yticks(range(0, 200,20)) #muda a escala 0,20,40,60
plt.ylabel('CAPEX (k€)') 
#plt.ylim([100,180])
plt.ylim([100,180])

#plt.yticks(range(100, 200,10))

plt.grid(axis='y',linestyle='--', linewidth=0.6)
plt.savefig('grafico\\capex_'+str(number_gw_descricao)+'.png')

plt.clf()
plt.close()
#plt.show()

'''
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
####################################### 
########### OPEX ##########
#######################################
'''
OPEX --> Custo operacional 
Cman -->  custo de operação e manutenção, que é 10%-15% do valor do CAPEX
Clease --> custo de aluguel, considerando que todo o locais de instalação serão alugados.
Celet  --> custo de eletricidade por ano
Ctrans --> custo de transmissão, que depende da tecnologia escolhida para Txinst (instalação de transmissão)
t --> que representa o tempo em anos
'''

#Cman=random.randint(10,15)/100 #10% -15% do valor do CAPEX (porcentagem random)
Cman=12.5/100 #considerando 12,5% metade do intervalo 10%-15%
Clease=1
Celet=1
Ctrans=0.1
t=1

#calculo OPEX
#OPEX=(Cman*CAPEX+ total_gw*(Clease + Celet + Ctrans))*t

#Todos os custos considera apenas o gateways, pois os custos
#dos dispositivos serão os mesmos  independente do algoritmo que escolhemos

#Conclusão: remover (Clease + Celet + Ctrans), deixando somente o gw
opex_grid_gw25=(Cman*capex_grid_gw25 + grid_gw25*(Clease + Celet + Ctrans ))*t
opex_grid_gw25=(Cman*capex_grid_gw25 + grid_gw25)*t

opex_gw_fuzzy=(Cman*capex_gw_fuzzy + gw_fuzzy*(Clease + Celet + Ctrans ))*t
opex_gw_fuzzy=(Cman*capex_gw_fuzzy + gw_fuzzy)*t

opex_gw_kmeans=(Cman*capex_gw_kmeans + gw_kmeans*(Clease + Celet + Ctrans ))*t
opex_gw_kmeans=(Cman*capex_gw_kmeans + gw_kmeans)*t

opex_gw_place=(Cman*capex_gw_place + gw_place*(Clease + Celet + Ctrans ))*t
opex_gw_place=(Cman*capex_gw_place + gw_place)*t


#opex_gw_rand16=(Cman*capex_gw_rand16 + gw_kmeans*(Clease + Celet + Ctrans ))*t
#opex_gw_rand16=(Cman*capex_gw_rand16 + gw_kmeans)*t

print("\n ---------------Dados OPEX----------------------------\n")
print("Valor opex_grid_gw25: ",opex_grid_gw25)
print("Valor opex_gw_fuzzy: ",opex_gw_fuzzy)
print("Valor opex_gw_Place_FCM: ",opex_gw_place)
#print("Valor opex_gw_rand16: ",opex_gw_rand16)

resultado_opex=(opex_gw_fuzzy/opex_grid_gw25)
result_opex=(1-resultado_opex)*100


resultado_opex_place=(opex_gw_place/opex_grid_gw25)
result_opex_place=(1-resultado_opex_place)*100

print("\nPorcentagem OPEX do fcm/grid25(%): ",result_opex)
print("Porcentagem OPEX do place/grid25(%): ",result_opex_place)

#+++++++++++++++++OPEX COLORIDO +++++++++++++++++++++++++++++++++++++++
#width=0.4
'''
plt.bar('Grid25', opex_grid_gw25, color=cor_grid25, align='center', width=0.6, hatch = hat_grid25)
#plt.bar('FCM', opex_gw_fuzzy, color=cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
plt.bar(nome_proposta, opex_gw_fuzzy, color=cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
plt.bar('Place', opex_gw_place, color=cor_place, align='center', width=0.5, hatch = hat_place)
#plt.bar('Kmeans', opex_gw_kmeans, color=cor_kmeans, align='center', width=0.5, hatch = hat_kmeans)
#plt.bar('rand16', opex_gw_rand16, color=cor_rand16, align='center', width=0.5, hatch = hat_rand16)

plt.ylabel('OPEX (k€)') 

plt.ylim([25,50])
plt.grid(axis='y',linestyle='--', linewidth=0.6)

plt.savefig('grafico\\opex_'+str(number_gw_descricao)+'.png')

plt.clf()
plt.close()
'''

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
########################################## 
########### CUSTO TOTAL CAPEX + OPEX #####
##########################################
#Somando capex e opex
soma_grid25=capex_grid_gw25 + opex_grid_gw25
soma_gw_fuzzy=capex_gw_fuzzy + opex_gw_fuzzy
soma_gw_kmeans=capex_gw_kmeans + opex_gw_kmeans
soma_gw_place=capex_gw_place + opex_gw_place
#soma_gw_rand16=capex_gw_rand16 + opex_gw_rand16

'''
#plt.figure(figsize=(8,4))
#++++++++++++++Capex e Opex Colorido +++++++++++++++++++++++++++++++++++
plt.bar('Grid25', soma_grid25, color=cor_grid25, align='center', width=0.6, hatch = hat_grid25)
plt.bar(nome_proposta, soma_gw_fuzzy, color=cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
#plt.bar('FCM', soma_gw_fuzzy, color=cor_fcm, align='center', width=0.6, hatch = hat_fuzzy)
plt.bar('Place', soma_gw_place, color=cor_place, align='center', width=0.5, hatch = hat_place)
#plt.bar('Kmeans', soma_gw_kmeans, color=cor_kmeans, align='center', width=0.5, hatch = hat_kmeans)
#plt.bar('rand16', soma_gw_rand16, color=cor_rand16, align='center', width=0.5, hatch = hat_rand16)


plt.ylabel('Custo total  (k€)')
#plt.ylabel('Total Cost (k€)')


#plt.yticks(range(0, 300,50)) #muda a escala 0,50,100,150

plt.ylim([100,250])
plt.grid(axis='y',linestyle='--', linewidth=0.6)

plt.savefig('grafico\\total_capex_opex_'+str(number_gw_descricao)+'.png')

plt.clf()
plt.close()
#plt.show()
'''

print("\n ---------------CUSTO TOTAL----------------------------\n")
print("Custo total grid_gw25: ",soma_grid25)
print("Custo total _gw_fuzzy: ",soma_gw_fuzzy)
print("Custo total _gw_fcm: ",soma_gw_place)
#print("Custo total _gw_rand16: ",soma_gw_rand16)

resultado_custo=(soma_gw_fuzzy/soma_grid25)
custo_total=(1-resultado_custo)*100

resultado_custo_place=(soma_gw_place/soma_grid25)
custo_total_place=(1-resultado_custo_place)*100

print("\nPorcentagem CUSTO TOTAL do fcm/grid25(%): ",custo_total)
print("Porcentagem CUSTO TOTAL do Place/grid25(%): ",custo_total_place)
print("\n *** FIM ***\n\n")
#=============================================================================================
#=============================================================================================
