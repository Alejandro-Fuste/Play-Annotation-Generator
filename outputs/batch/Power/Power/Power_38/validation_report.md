# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_38`
- **Input XML**: `outputs/batch/Power/Power/Power_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [12-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-63] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-232] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-118] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [124-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-268] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-228] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-250] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-222] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-206] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-232] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-222] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-30] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-207] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-258] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-268] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-269] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.