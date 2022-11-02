import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function Profile({media}) {
  return (
    <Card sx={{ maxWidth: 1000, maxHeight: 1920, ml:10 }}>
      <CardMedia
        component="img"
        height="500"
        width="1000"
        image={media.poster_path}
      />

      <CardContent>
      <Typography  gutterBottom variant="h5" component="div">
          {media.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {media.name}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Share</Button>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  );
}