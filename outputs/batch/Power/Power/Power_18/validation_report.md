# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_18`
- **Input XML**: `outputs/batch/Power/Power/Power_18/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [22-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-240] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-226] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-213] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-253] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-269] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '23' has 1 frames without a visible bounding box.
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