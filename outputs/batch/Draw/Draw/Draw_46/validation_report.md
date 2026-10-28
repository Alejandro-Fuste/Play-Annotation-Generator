# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_46`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 92: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '1' (C): higher_priority='Action_BallSnap' [38–57], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=58.
> - Action 'Action_None' range [114-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-230] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-96] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-184] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-231] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-123] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-101] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-179] for track '18' has 2 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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