import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function ForumItem({forum}) {
  return (
    <Card sx={{ maxWidth: 1000, maxHeight: 1920, ml:50}}>
      <CardContent>
      <Typography  gutterBottom variant="h5" component="div">
          {forum.title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          {forum.name}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Share</Button>
      </CardActions>
    </Card>
  );
}