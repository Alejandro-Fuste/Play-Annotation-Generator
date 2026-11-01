# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_201`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_BallCarry' for track '9' has invalid range: start=306, end=162. Clamping end to start.
> - Action 'Action_PreSnap' range [0-222] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-362] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-372] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-383] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-319] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-332] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [296-303] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [305-316] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-371] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-385] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [266-278] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-375] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-320] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-351] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [293-300] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-294] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-380] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-398] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-412] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [266-278] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-347] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-368] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-381] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [266-276] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [291-324] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-346] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-361] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-366] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-375] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-419] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-295] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-311] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-324] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-337] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-353] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-370] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-419] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-342] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-334] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-360] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-407] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-366] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-414] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-400] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [380-406] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-419] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-394] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-407] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [393-403] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-416] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '27' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.