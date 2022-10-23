import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Spacer from '../style/Spacer';
import CarouselItem from './CarouselItem';
import Carousel from 'react-material-ui-carousel';
import ForumItem from './ForumItem';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

function BasicTabs() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%', mt:10}}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider'}}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example" sx={{ ml:100}}>
          <Tab label="Movies" {...a11yProps(0)} />
          <Tab label="Series" {...a11yProps(1)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <MovieKatalogue />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <SeriesKatalogue />
      </TabPanel>
      <TabPanel value={value} index={2}>
        Item Three
      </TabPanel>
    </Box>
  );
}



function MovieKatalogue(){

    return(
      <div>
    <Carousel >
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
      </div>
    
    )
}

function SeriesKatalogue(){
  return(
    <div>
  <Carousel >
                                  <CarouselItem media={{
      title : 'House of Dragons',
      poster_path : 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/z2yahl2uefxDCl0nogcRBstwruJ.jpg',
      name : 'House of dragons name',
      release_date : '2022'
    }} />
                                  <CarouselItem media={{
          title : 'Lord of the Rings - Rings of Power',
          poster_path : 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mYLOqiStMxDK3fYZFirgrMt8z5d.jpg',
          name : 'Rings of Power',
          release_date : '2099'
      }}/>
                                  <CarouselItem media={{
              title : 'Chainsaw Man',
              poster_path : 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/npdB6eFzizki0WaZ1OvKcJrWe97.jpg',
              name : 'Chainsaw name',
              release_date : '2022',
          }}/>
    </Carousel>
    </div>
  
  )
}

export default BasicTabs;

