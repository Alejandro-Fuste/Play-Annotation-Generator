# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_63`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_63/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 126: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [49–66], lower_priority='Action_PassBlock' annotated_start=52, effective_Action_PassBlock_start=67.
> - Action 'Action_None' range [49-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-323] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-320] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-275] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-157] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [159-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-222] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-105] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-329] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-328] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-287] for track '28' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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