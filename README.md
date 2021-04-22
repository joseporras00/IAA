# IAA
if(col<(soup.cols()-1)){
                    aux = soup.cell(row,col+1);
                    if (node->has(aux))//RIGHT
                    scan_cell(row,col+1,0,1,soup,node,scan_result);
                    }

                    if(row>0 && scan_result.first == ""){
                    aux = soup.cell(row-1, col);
                    if (node->has(aux))//UP
                    scan_cell(row-1,col,-1,0,soup,node,scan_result);
                    }

                    if(col>0 && scan_result.first == ""){
                    aux = soup.cell(row, col-1);
                    if (node->has(aux)) //LEFT  
                    scan_cell(row,col-1,0,-1,soup,node,scan_result);
                    }
                    
                    if(row<(soup.rows()-1)&& scan_result.first == ""){
                    aux = soup.cell(row+1, col);
                    if (node->has(aux)) //DOWN  
                    scan_cell(row+1,col,+1,0,soup,node,scan_result);
                    }

                    if(col<(soup.cols()-1) && row>0 && scan_result.first == ""){
                    aux = soup.cell(row-1,col+1);
                    if (node->has(aux))// UP RIGHT
                    scan_cell(row-1,col+1,-1,1,soup,node,scan_result);
                    }

                    if(col>0 && row>0 && scan_result.first == ""){
                    aux = soup.cell(row-1, col-1);
                    if (node->has(aux)) // UP LEFT  
                    scan_cell(row-1,col-1,-1,-1,soup,node,scan_result);
                    }

                    if(col<(soup.cols()-1)&& row<(soup.rows()-1)&& scan_result.first == ""){
                    aux = soup.cell(row+1,col+1);
                    if (node->has(aux))//DOWN RIGHT
                    scan_cell(row+1,col+1,1,1,soup,node,scan_result);
                    }

                    if(col>0 && row<(soup.rows()-1) && scan_result.first == ""){
                    aux = soup.cell(row+1, col-1);
                    if (node->has(aux)) //DOWN LEFT  
                    scan_cell(row+1,col-1,1,-1,soup,node,scan_result);
                    }
