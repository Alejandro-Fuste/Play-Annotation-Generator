# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_186`
- **Input XML**: `outputs/batch/Power/Power/Power_186/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 374: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [6-81] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-157] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-251] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-285] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-253] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-216] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-88] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-266] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-292] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-258] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-283] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-132] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-247] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-246] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-133] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-329] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-229] for track '23' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.