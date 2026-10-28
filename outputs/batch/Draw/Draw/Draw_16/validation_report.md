# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_16`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 34: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [43–55], lower_priority='Action_PassBlock' annotated_start=47, effective_Action_PassBlock_start=56.
> - Action 'Action_PassBlock' range [47-81] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-242] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [247-253] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-264] for track '6' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [43-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-125] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [43-69] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-88] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-111] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 43, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [43-49] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-69] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-136] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-204] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-261] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-263] for track '29' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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