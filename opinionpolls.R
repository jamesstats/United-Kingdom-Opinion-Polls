library(tidyverse)
library(rvest)
library(janitor)  

wiki <-"https://en.wikipedia.org/wiki/Opinion_polling_for_the_next_United_Kingdom_general_election#National_poll_results"
wiki_html<-read_html(wiki) 
wiki_tab<-wiki_html%>%html_table(fill = TRUE)
u_k<-wiki_tab[[2]]
u_k_2<-wiki_tab[[3]]
#deleting columns
u_k$Samplesize<-NULL
u_k$Reform<-NULL
u_k$Others<-NULL
u_k$Client<-NULL
#renaming columns
colnames(u_k)<-c('Date','Pollster','Area','Con','Lab','LibDem','SNP','Green','Lead')
#deleting row
u_k<-u_k[-c(1),]
u_k<-u_k[-c(47),]
u_k<-u_k[-c(69),] 
write_csv(u_k,paste0('data/',Sys.Date(),'_OpinionPolls','.csv'))   
