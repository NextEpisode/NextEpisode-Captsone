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
import BasicTable from './Table';
import Paper from '@mui/material/Paper';
import EnhancedTable from './SortingTable';


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
  let isMovie = true;

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: '100%'}}>
      <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs value={value} onChange={handleChange} aria-label="basic tabs example" sx={{ ml: 100 }}>
          <Tab label="Movies" {...a11yProps(0)} />
          <Tab label="Series" {...a11yProps(1)} />
        </Tabs>
      </Box>
      <TabPanel value={value} index={0}>
        <ProfileBody isMovie={true} medias={[{
          title: 'Shrek',
          poster_path: 'https://www.themoviedb.org/t/p/original/iB64vpL3dIObOtMZgX3RqdVdQDc.jpg',
          status: 'Watched',
          category: 'Action/Adventure',
          release_date: '2001'
        },{
          title: 'Dune',
          poster_path: 'https://imageio.forbes.com/specials-images/imageserve/61116cea2313e8bae55a536a/-Dune-/0x0.jpg?format=jpg&width=960',
          status: 'Planning to watch',
          category: 'SciFi',
          release_date: '2022',
        },{
          title: 'Robinhood',
          poster_path: 'https://movieposters2.com/images/1595344-b.jpg',
          status: 'Watched',
          category: 'Action/Adventure',
          release_date: '2099'
        }]}/>
      </TabPanel>
      <TabPanel value={value} index={1}>
        <ProfileBody isMovie={false} medias={[{
          title: 'House of Dragons',
          poster_path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/z2yahl2uefxDCl0nogcRBstwruJ.jpg',
          release_date: '2022',
          category: 'Drama',
          status: 'Dropped',
          episode: '0'
        },{
          title: 'Lord of the Rings - Rings of Power',
          poster_path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mYLOqiStMxDK3fYZFirgrMt8z5d.jpg',
          release_date: '2099',
          category: 'Action/Adventure',
          status: 'Planning to watch',
          episode: '0'
        },{
          title: 'Chainsaw Man',
          poster_path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/npdB6eFzizki0WaZ1OvKcJrWe97.jpg',
          release_date: '2022',
          category: 'Action/Adventure',
          status: 'Planning to watch',
          episode: '0'
        }]}/>
      </TabPanel>
    </Box>
  );
}



function ProfileBody({medias,isMovie}) {
  return (
    <div>
      <Carousel>
        {medias.map((media) => (
          <CarouselItem media={media} />
        ))}
      </Carousel>
      <Container>
        <Typography variant="h4" >
          Katalogue
        </Typography>
        <EnhancedTable medias={medias}></EnhancedTable>
        {/* <BasicTable medias={medias} isMovie={isMovie} /> */}
      </Container>
    </div>

  )
}

export default BasicTabs;

