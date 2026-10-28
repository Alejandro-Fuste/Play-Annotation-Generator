# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_97`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [137-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-86] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-181] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-139] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-93] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-155] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 40, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [40-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-196] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.