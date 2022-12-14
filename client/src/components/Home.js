import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CameraIcon from '@mui/icons-material/PhotoCamera';
import CardMedia from '@mui/material/CardMedia';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Carousel from 'react-material-ui-carousel';
import { MediaCard } from './MediaCard';
import CarouselItem from './CarouselItem';




// const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];



const theme = createTheme();

export default function Album() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />

            <main>
                {/* Hero unit */}
                <Container sx={{ py: 8 }} >
                    {/* End hero unit */}
                                <Carousel
                                    >
                                    <CarouselItem media={{
        title : 'Shrek',
        poster_path : 'https://www.themoviedb.org/t/p/original/iB64vpL3dIObOtMZgX3RqdVdQDc.jpg',
        name : 'Shrek name',
        release_date : '2001'
      }} />
                                    <CarouselItem media={{
            title : 'Robinhood',
            poster_path : 'https://movieposters2.com/images/1595344-b.jpg',
            name : 'Robinhood name',
            release_date : '2099'
        }}/>
                                    <CarouselItem media={{
                title : 'Dune',
                poster_path : 'https://imageio.forbes.com/specials-images/imageserve/61116cea2313e8bae55a536a/-Dune-/0x0.jpg?format=jpg&width=960',
                name : 'Dune name',
                release_date : '2022',
            }}/>
                                </Carousel>
                </Container>
            </main>

        </ThemeProvider>
    );
}