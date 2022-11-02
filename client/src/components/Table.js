import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { CardMedia, IconButton } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';



export default function BasicTable({medias,isMovie}) {
    if(isMovie){
        return MovieTable({medias});
    }
    else{
        return SeriesTable({medias});
    }
}

function MovieTable({medias}){
    return(
<TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Poster </TableCell>
            <TableCell align="left">Name</TableCell>
            <TableCell align="right">Title</TableCell>
            <TableCell align="right">Release Date</TableCell>
            <TableCell align="right">Category</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {medias.map((media) => (
            <TableRow
              key={media.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">
                <CardMedia
                    component="img"
                    height="100"
                    width="100"
                    image={media.poster_path}
                />
              </TableCell>
              <TableCell component="th" scope="row">
                {media.name}
              </TableCell>
              <TableCell align="right">{media.title}</TableCell>
              <TableCell align="right">{media.release_date}</TableCell>

              <TableCell align="right">{media.name}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    );
}

function SeriesTable({medias}){
    let episodes = 0;
    return(
        <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Poster </TableCell>
            <TableCell align="left">Name</TableCell>
            <TableCell align="right">Title</TableCell>
            <TableCell align="right">Release Date</TableCell>
            <TableCell align="right">Episode</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {medias.map((media) => (
            <TableRow
              key={media.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">
                <CardMedia
                    component="img"
                    height="100"
                    width="100"
                    image={media.poster_path}
                />
              </TableCell>
              <TableCell component="th" scope="row">
                {media.name}
              </TableCell>
              <TableCell align="right">{media.title}</TableCell>
              <TableCell align="right">{media.release_date}</TableCell>
              <TableCell align="right">{media.episode}<IconButton color="primary" onClick={addToEpisodes(episodes)}><AddIcon fontSize="small" /> 
      </IconButton></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    );
}

function addToEpisodes(episodes){
    episodes++;
}
