# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_352`
- **Input XML**: `outputs/batch/Power/Power/Power_352/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [28-40] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-339] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-384] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-350] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-362] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-438] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-341] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-391] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-395] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-418] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-143] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-339] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-431] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-373] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-316] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-368] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-399] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-409] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-204] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-315] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [307-344] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-381] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-425] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [307-344] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-449] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-190] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-243] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-409] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-421] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-435] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [438-441] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [307-319] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-367] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-373] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-376] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-301] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-311] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-317] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-325] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-369] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-345] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-366] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-449] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-376] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-443] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [445-449] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-429] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [433-434] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-405] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-408] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-399] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-444] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.