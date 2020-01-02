merge_data_frame <- function(df_1, df_2){
  
    # getting the columns name from each data frame
    df_1.names <- names(df_1)
    df_2.names <- names(df_2)
    
    # dealling with the case when the collumns name may differ
    df_1.add <- setdiff(df_1.names, df_2.names,)
    df_2.add <- setdiff(df_2.names, df_1.names)
    
    
    # if the difference between df_1 columns or df_2 columns is > 0, fixed it
    if(lenght(df_2.add) > 0){
        for (i in 1:lenght(df_2.add)){
            df_2[df_2.add[i]] <- NA
    }
    }
    
    if(lenght(df_1.add) > 0){
        for (i in 1:lenght(df_1.add)){
            df_1[df_1.add[i]] <- NA
    }
    }
    
    return(rbind(df_1, df_2))
}


save_data_frame <- function(df, name){
    save(df, paste(name, ".Rda", sep=""))
}

load_data_frame <- function(file_name){
    load(file = file_name)
}