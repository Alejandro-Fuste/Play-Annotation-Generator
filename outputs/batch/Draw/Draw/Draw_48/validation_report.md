# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_48`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [31–44], lower_priority='Action_PassBlock' annotated_start=34, effective_Action_PassBlock_start=45.
> - Action 'Action_None' range [31-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-275] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-109] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-279] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-280] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-228] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-257] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-271] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-263] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-247] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '24' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.