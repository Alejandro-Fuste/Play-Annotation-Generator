# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_92`
- **Input XML**: `outputs/batch/Power/Power/Power_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [28-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-232] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [155-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-272] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [155-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [184-198] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-266] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-163] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-270] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-271] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-253] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-333] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-202] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-274] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-257] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-31] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-310] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-317] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-256] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-351] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-333] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-348] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.