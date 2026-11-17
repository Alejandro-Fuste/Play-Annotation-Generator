# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_181`
- **Input XML**: `outputs/batch/Power/Power/Power_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 364: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [23-236] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-60] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-182] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-233] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-277] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-308] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [170-203] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-188] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-252] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [304-310] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.