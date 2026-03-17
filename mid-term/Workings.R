df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/Netflix.csv')
df |> filter(release_year==2018)|>
  mutate(
    size = str_count(cast,',')+1
  )|>
  filter(size>=10)
df|>filter(rating=='TV-14')|>
  mutate(s = mean(SpecialScore))
df|>
  group_by(country)|>
  count()|>
  arrange(-n)

df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/Sleep_health_and_lifestyle_dataset.csv')
unique(df$Occupation)
df2<-df |> filter(Stress.Level>=8) |> group_by(Person.ID) |> 
  summarize(n = n())
df |> group_by(BMI.Category) |>
  summarize(med = median(Age))
df |> 
  filter(Quality.of.Sleep==9|Quality.of.Sleep==10)|>
  mutate(med=median(Age))

df |>
  group_by(Occupation) |>
  summarise(avg_qos = mean(Quality.of.Sleep)) |>
  arrange(-avg_qos)

df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/PokemonData.csv')
df |> filter(Generation==1) |> filter(is.na(Type2)|Type2=='')|>count()
typeof(df$Legendary)

df |> filter(Legendary==FALSE) |> filter(Generation>=4) |> filter(is.na(Type2)|Type2=='')|>
  group_by(Type1) |>
  summarize(med_speed = median(Speed))|>
  arrange(-med_speed)

t1 <- unique(df$Type1)
t2 <- unique(df$Type2)
mean(t1 %in% t2)

df |> filter(str_detect(Name, '(Mega )'))
df |> group_by(Num) |> count() |> filter(n>1)


df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/Titanic_train.csv')
df$Survived |> mean()
ifelse(is.na(df$Age),"None",df$Age)


df |> filter(Sex=='male') |> summarise(r = mean(Survived))
df |> filter(Embarked == 'S') |> count()

df |> filter(is.na(Age)|Age=='') |> count()
df |> filter(!is.na(Cabin)&Cabin!='') |> count()
df |> count()

df |> filter(between(Age,0,12)) |>
  summarise(r = mean(Survived))

df |> head(1) |> select(Age)

df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/kpopidolsv3.csv')
df |> filter(!is.na(Second.Country)&Second.Country!='')

df |> filter(Gender=='F'&!is.na(Height)) |>group_by(Group,Company) |>
  summarise(
    n = n(),
    avg_h = mean(Height,na.rm=T)
  ) |>
  arrange(-avg_h)

df$Group |> unique()

df |> filter(Gender=='F') |> count()
df |> arrange(-Height) |>
  mutate(n = Full.Name) |> head(1)

df <- read.csv('http://www.bio8.cs.hku.hk/comp2501/vgsales.csv')
colnames(df)

df |>
  group_by(Publisher) |>
  summarise(
    n = count(name)
  )

df |> filter(Rating>4)
df$Platform |> unique()

df |> filter(Platform %in% c('PS','PS2','PS3','PS4','PSP'))

df |> mutate(div = abs(NA_Sales-JP_Sales)) |>
  arrange(-div)|>head(1)
?rename

df |> rename(hi=Global_Sales)

df <- dplyr::murders
df |> group_by(cyl) |> filter(hp>100) |> summarize(mean(mpg))


