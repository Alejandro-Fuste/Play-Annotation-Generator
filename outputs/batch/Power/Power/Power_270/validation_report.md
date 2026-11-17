# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_270`
- **Input XML**: `outputs/batch/Power/Power/Power_270/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 29 |
| Ball Tracks | 2 |
| CSV events parsed | 10 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 540: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [30-304] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-333] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-366] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-383] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-322] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [239-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [259-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [264-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-389] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-389] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-331] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-160] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-302] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-255] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-319] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-361] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-315] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-376] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-380] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-381] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-385] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.