# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_303`
- **Input XML**: `outputs/batch/Power/Power/Power_303/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_DownBlock' for track '23' has invalid range: start=284, end=74. Clamping end to start.
> - Action 'Action_DownBlock' range [284-300] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [311-318] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [323-325] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-381] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-330] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-82] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-126] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-304] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-309] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-327] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-346] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-419] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-380] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-387] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-419] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-323] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-394] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-330] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-40] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-312] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-43] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-325] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-339] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-351] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-374] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-419] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-396] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-401] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-411] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-349] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-308] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-322] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-38] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-309] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-348] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-419] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-335] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-351] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-339] for track '29' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.