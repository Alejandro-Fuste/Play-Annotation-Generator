# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `KickoffReturnTouchdown_42`
- **Input XML**: `outputs/batch/KickoffReturnTouchdown/KickoffReturnTouchdown/KickoffReturnTouchdown_42/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/KickoffReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 69 |
| Player Tracks | 69 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 239 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 659 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 659 as fallback play end.
> - Segment 'Action_CrossGoalLine' for track '1' has invalid range: start=632, end=455. Clamping end to start.
> - Action 'Action_None' range [15-238] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-328] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-348] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-368] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-376] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-392] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [241-295] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [302-366] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [368-455] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-225] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-278] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-280] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-335] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-355] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-377] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-390] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-353] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-362] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [366-370] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-377] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-392] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-298] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-347] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-171] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-412] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-540] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-543] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-549] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-222] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-257] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-273] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-353] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [355-369] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-386] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-401] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-425] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-451] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-616] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [625-635] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-648] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-279] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-345] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-370] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-417] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-388] for track '9' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [15-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-283] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-365] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [15-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-236] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-335] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-266] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-303] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [15-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-314] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [322-338] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [341-354] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-361] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-375] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-638] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [645-659] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-407] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [411-438] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-449] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-247] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [250-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-267] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [288-296] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-395] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 15, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [15-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-218] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-256] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-272] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-321] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-256] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-281] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-325] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-341] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-356] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-379] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-388] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-403] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-471] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [510-512] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-384] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-393] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-552] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [554-593] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [605-625] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [627-630] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-399] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-404] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-410] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [412-418] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-354] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-578] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-370] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-376] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-413] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [376-402] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-413] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-395] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [452-462] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-501] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [503-504] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-402] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-422] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [425-557] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-652] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [654-656] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-418] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-589] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [423-509] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-560] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [425-432] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-436] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-482] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [432-434] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [451-478] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-485] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-549] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-645] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [647-656] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-507] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [513-515] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [517-529] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [531-532] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-636] for track '49' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [639-642] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [507-510] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [515-635] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-639] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [520-532] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-525] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [552-573] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [575-624] for track '53' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-564] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-633] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [635-636] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [638-641] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [647-649] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-584] for track '56' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [581-606] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-591] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-625] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-648] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [605-656] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [633-645] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [647-659] for track '63' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.