# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_59`
- **Input XML**: `outputs/batch/Power/Power/Power_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [20-255] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-275] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-280] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-286] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-176] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [178-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-264] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-297] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-259] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-187] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-190] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-219] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-299] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.