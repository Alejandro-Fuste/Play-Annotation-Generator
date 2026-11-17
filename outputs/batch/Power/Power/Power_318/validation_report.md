# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_318`
- **Input XML**: `outputs/batch/Power/Power/Power_318/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 45 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 636: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [21-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-236] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-291] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [155-230] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-176] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-289] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-187] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-261] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-299] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.