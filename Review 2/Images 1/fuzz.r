install.packages("fcm")
library(fcm)
act.vec <- data.frame(1, 1, 1, 0, 0, 0 )    
colnames(act.vec) <- c("C1", "C2", "C3", "C4", "C5", "C6") 

C1 = c(0.0, 1.0, 0.0, 0.0, 0.0, 0.0)
C2 = c(0.0, 0.0, 1.0, 0.0, 0.0, 0.0)
C3 = c(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
C4 = c(0.0, 0.0, 0.0, 0.0, 0.0, 1.0)
C5 = c(0.0, 0.0, 1.0, 1.0, 0.0, 0.0)
C6 = c(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



w.mat <- matrix(c(C1, C2, C3, C4, C5, C6), nrow =6, ncol=6, byrow=TRUE)   
w.mat <- as.data.frame(w.mat)   
colnames(w.mat) <- c("C1", "C2", "C3", "C4", "C5", "C6") 
w.mat      
output1 <- fcm.infer(act.vec, w.mat)
output2 <- fcm.infer(act.vec, w.mat, 35, "k", "b", lambda = 2, e = 0.0001)
output2$values  
library (reshape2)
library (ggplot2)
iterations <- as.numeric(rownames(output1$values))  
df <- data.frame(iterations, output1$values)   
df2 <- melt(df, id="iterations")              
ggplot(data=df2,                              
       aes(x=iterations, y=value, group=variable, colour=variable)) +
       theme_bw() + geom_line(size=0.7) + geom_point(size = 3)
iterations <- as.numeric(rownames(output2$values))  
df <- data.frame(iterations, output2$values)   
df2 <- melt(df, id="iterations")              
ggplot(data=df2,
       aes(x=iterations, y=value, group=variable, colour=variable)) +
       theme_bw() + geom_line(size=0.7) + geom_point(size = 3)