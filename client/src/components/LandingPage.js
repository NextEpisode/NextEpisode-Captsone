import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Button from '@mui/material/Button';
import CameraIcon from '@mui/icons-material/PhotoCamera';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Item from '@mui/material/ListItem';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import ShareIcon from '@mui/icons-material/Share';
import ChatBubbleIcon from '@mui/icons-material/ChatBubble';
import PhoneIphoneIcon from '@mui/icons-material/PhoneIphone';
import BrushIcon from '@mui/icons-material/Brush';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Carousel from 'react-material-ui-carousel';

function Copyright() {
    return (
        <Typography variant="body2" color="text.secondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://mui.com/">
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

// const cards = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const theme = createTheme();

export default function Album() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <main>
                {/* Hero unit */}
                <Box
                    sx={{
                        bgcolor: 'info.main',
                        pt: 8,
                        pb: 6,
                        marginLeft: 50,
                        marginRight: 50,
                        borderRadius: 7,

                    }}
                >
                    <Typography
                        component="h1"
                        variant="h2"
                        align="center"
                        color="text.primary"
                        gutterBottom
                    >
                        Album layout
                    </Typography>
                    <Typography variant="h5" align="center" color="text.secondary" paragraph>
                        Something short and leading about the collection below—its contents,
                        the creator, etc. Make it short and sweet, but not too short so folks
                        don&apos;t simply skip over it entirely.
                    </Typography>
                    <Grid 
                        container   
                        direction="row"
                        justifyContent="space-around"
                        alignItems="center" rowSpacing={5}  columns={10}>
                        <Grid item xs={4}>

                            <Item>
                                <ShareIcon sx={{ mr: 2 }}></ShareIcon>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in porta sem, id maximus libero. Donec hendrerit lobortis turpis, et iaculis nibh imperdiet luctus.
                            </Item>
                        </Grid>
                        <Grid item xs={4}>
                            <Item>
                                <PhoneIphoneIcon sx={{ mr: 2 }}></PhoneIphoneIcon>

                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in porta sem, id maximus libero. Donec hendrerit lobortis turpis, et iaculis nibh imperdiet luctus.
                            </Item>
                        </Grid>
                        <Grid item xs={4}>
                            <Item>
                                <ChatBubbleIcon sx={{ mr: 2 }}></ChatBubbleIcon>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in porta sem, id maximus libero. Donec hendrerit lobortis turpis, et iaculis nibh imperdiet luctus.
                            </Item>
                        </Grid>
                        <Grid item xs={4}>
                            <Item>
                                <BrushIcon sx={{mr: 2}}></BrushIcon>
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in porta sem, id maximus libero. Donec hendrerit lobortis turpis, et iaculis nibh imperdiet luctus.

                            </Item>
                        </Grid>
                    </Grid>
                    <Stack
                        sx={{ pt: 4 }}
                        direction="row"
                        spacing={2}
                        justifyContent="center"
                    >
                        <Button variant="contained">Main call to action</Button>
                    </Stack>
                </Box>
                <Container sx={{ py: 8 }} maxWidth="md">
                    {/* End hero unit */}
                                <Carousel
                                    sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                                    <CardMedia
                                        component="img"
                                        sx={{maxHeight: 700, maxWidth:700}}

                                        image="https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx114745-APZN90WhNMAD.jpg"
                                        alt="random"
                                    />
                                    <CardMedia
                                        component="img"
                                        sx={{maxHeight: 700, maxWidth:700}}

                                        image="https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/nx21-tXMN3Y20PIL9.jpg"
                                        alt="random"
                                    />
                                    <CardMedia
                                        component="img"
                                        sx={{maxHeight: 700, maxWidth:700, borderRadius: 2}}

                                        image="https://s4.anilist.co/file/anilistcdn/media/anime/cover/large/bx130592-LAUlhx15mxQu.jpg"
                                        alt="random"
                                    />
                                </Carousel>
                </Container>
            </main>
            {/* Footer */}
            <Box sx={{ bgcolor: 'background.paper', p: 6 }} component="footer">
                <Typography variant="h6" align="center" gutterBottom>
                    Footer
                </Typography>
                <Typography
                    variant="subtitle1"
                    align="center"
                    color="text.secondary"
                    component="p"
                >
                    Something here to give the footer a purpose!
                </Typography>
                <Copyright />
            </Box>
            {/* End footer */}
        </ThemeProvider>
    );
}