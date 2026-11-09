# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_123`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 129 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PressEdge' range [115-137] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-222] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-275] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-343] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-388] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-449] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-231] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-449] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-207] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-219] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-288] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-372] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-230] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-287] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-300] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-114] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-78] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-148] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-214] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-311] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-371] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-278] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-334] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-270] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-392] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-420] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-248] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-288] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-304] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-287] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-294] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-337] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-400] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-230] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-241] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-353] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-416] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-449] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-319] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-380] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-416] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-305] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-370] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-279] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-377] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-414] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-449] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-282] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-369] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-315] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-333] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-355] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-449] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-375] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-391] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-394] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-411] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [416-421] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-429] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-439] for track '39' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.