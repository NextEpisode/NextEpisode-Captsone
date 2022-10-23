import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Spacer from '../style/Spacer';


function Profile(){
    return(
    <Box
        sx={{
          width: 1980,
          height: 300,
          backgroundColor: 'primary.dark',
          // '&:hover': {
          //   backgroundColor: 'primary.main',
          //   opacity: [0.9, 0.8, 0.7],
          // },
          mt:8
        }}>
          <Spacer axis='vertical' size={100}></Spacer>
        <Avatar src="/static/images/avatar/avatar.png" variant="square" sx={{width: 200, height: 200,ml:20}}/>
    </Box>
    )
}

export default Profile;

